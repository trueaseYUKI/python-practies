import argparse
import  logging
import math
from datetime import datetime
from typing import Tuple, List, Optional
from pathlib import Path
# 获取文件的MIME类型
import mimetypes
# 队列
from collections import deque


class FileInfo:
    def __init__(self,path,name,type,size,update_time,depth):
        self.path = path
        self.name = name
        self.type = type
        self.size = size
        self.update_time = update_time
        self.depth = depth

    def __str__(self):
        return f"name: {self.name}, path: {self.path}, type：{self.type}, size：{self.size}B, update_time：{self.update_time}, depth：{self.depth} "

    def __repr__(self):
        return self.__str__()


def cli_input_arg():
    arg_parse = argparse.ArgumentParser()
    # 根文件路径参数
    arg_parse.add_argument("root_path",type=str,help="文件系统的根路径 required")
    # 是否递归子目录（填写这参数就递归遍历目录）
    arg_parse.add_argument("--recursive","-R",action="store_true",help="是否递归子目录")
    # 是否对当前目录下的文件进行统计
    arg_parse.add_argument("--statistics","-S",type=str,help="是否对当前文件夹下的文件进行统计type/date/mime",default="None")
    # 是否跟随符号链接（可选参数）
    arg_parse.add_argument("--follow","-fl",action="store_true",default=False,help="是否跟随符号链接,会去找.lnk的实际地址")
    # 输出报告的文件路径（JSON 或 CSV）
    arg_parse.add_argument("--report_path","-r",type=str,help="将扫描的结果生成报告保存到你指定的位置")
    # 指定使用对应的查重算法（这里用 -h 会与argparse内部的 -h参数冲突，所以使用-ha）
    arg_parse.add_argument("--hash_algorithm","-ha",type=str,help="你指定选择对文件查重使用什么算法,默认SHA-256",default="SHA-256")
    # 小于多少字节(B)可以跳过hash
    arg_parse.add_argument("--min_file_size_for_hash","-m",type=int,help="小于多少字节（B）可以跳过hash查重")
    # 日志等级
    arg_parse.add_argument("--log","-l",type=str,help="选择日志等级INFO/DEBUG/ERROR（默认INFO）",default="INFO")
    # 输出报告的格式
    arg_parse.add_argument("--format","-f",type=str,help="报告输出的格式CSV/JSON（默认JSON）",default="JSON")

    return arg_parse
    pass


# 格式化非递归遍历文件夹
def format_non_recursion_output(file_content:List[FileInfo]):
    """
    格式化输出非递归方式的文件夹访问
    :param file_content:
    :return:
    """
    for item in file_content:
        print(f"- {item.name}\t{item.type}\t{item.size}B\t{item.update_time}\t{item.path}")
    pass


def format_recursion_output(stack: deque[Tuple[Path, int]], is_follow=False):
    """
    格式化输出递归方式的文件夹访问（深度优先遍历）
    :param stack: 栈，存储(路径, 深度)元组
    :param is_follow: 是否跟随符号链接
    :return:
    """
    while stack:
        # 从栈顶弹出（深度优先）
        root_path, depth = stack.pop()

        try:
            # 先打印当前目录信息
            modify_time = root_path.stat().st_mtime
            size = root_path.stat().st_size
            time_stamp = datetime.fromtimestamp(modify_time)
            format_time = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
            file_type = 'dir'
            name = root_path.name

            print(f"{'-' * (depth * 2)} {name}\t {file_type}\t {size}B\t {format_time}\t")

            # 收集子目录，稍后压入栈中（保证正确的遍历顺序）
            subdirs = []

            # 遍历当前目录下的所有项目
            for item in root_path.iterdir():
                modify_time = item.stat().st_mtime
                size = item.stat().st_size
                time_stamp = datetime.fromtimestamp(modify_time)
                format_time = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
                name = item.name

                if item.is_file():
                    # 处理文件
                    file_type, encoding = mimetypes.guess_type(name)
                    if file_type is None:
                        file_type = item.suffix[1:] if item.suffix else 'unknown'


                    print(f"{'-' * ((depth + 1) * 2)} {name}\t {file_type}\t {size}B\t {format_time}\t")

                elif item.is_symlink():
                    # 处理符号链接
                    file_type = 'lnk'
                    print(f"{'-' * ((depth + 1) * 2)} {name}\t {file_type}\t {size}B\t {format_time}\t")

                elif item.is_dir():
                    # 收集子目录，后续统一处理
                    subdirs.append(item)

            # 将子目录按逆序压入栈中（保证正确的遍历顺序）
            for subdir in reversed(subdirs):
                stack.append((subdir, depth + 1))

        except Exception as e:
            print(f"scan root path find Error:{e}")
    pass


# 1.遍历指定目录
def traverse_content(path_str:str,is_recursive:bool=False,is_follow:bool=False):
    """
    遍历文件夹（分为递归和非递归）
    非递归：只会显示第一层
    递归会将所有文件夹的内部全部显示
    :return:
    """
    file_content = None
    # 1.如果路径参数不存在或者为空串，则直接返回
    if(path_str == None or not path_str.strip()):
        print("Please don't input empty path string")
        return

    current_path = Path(path_str)

    # 2.判断文件目录是否存在
    if(not current_path.exists() or  not current_path.is_dir()):
        print("that path not exist or that isn't directory")
        return

    # 3.进行遍历
    file_structs = []
    if(is_recursive):
        # 遍历式递归
        # 修改为广度优先遍历实现栈
        queue = deque([(current_path,0)])
        format_recursion_output(queue,is_follow=is_follow)
        pass
    else:
        # 非递归遍历
        for item in current_path.iterdir():
                # 1.生成FileInfo对象
                file_type = 'dir'
                size = item.stat().st_size
                modify_time = datetime.fromtimestamp(current_path.stat().st_mtime)
                formatted_time = modify_time.strftime("%Y-%m-%d %H:%M:%S")
                if item.is_file():
                    # 先猜它的MIME 类型
                    file_type,encoding = mimetypes.guess_type(item.name)
                    if(file_type == None):
                        # 没有就用后缀名表示
                        file_type = item.suffix[1:]
                    pass
                elif item.is_symlink():
                    file_type = 'lnk'
                file_info = FileInfo(item,item.name,file_type,size,formatted_time,1)
                # 加入到file_struct_list中
                file_structs.append(file_info)
        format_non_recursion_output(file_structs)
        pass
        # 3.2.显示当前文件夹的第一层的文件

    pass




# statistics 模块
def statistics_file_size(item:FileInfo,non_statistics:bool=True,way="type"):
    """
    文件大小统计方法
    :param path: 根路径
    :param non_statistics: 不进行统计
    :param way: 统计方式
    :return:
    """
    # 1.先判断是否需要统计


    pass

# 格式化统计结果
def format_statistics_result(root_path:str,way:Optional[str]):
    if(way == "None"): return

    file_dict = {}
    # 1.获取根路径
    root = Path(root_path)
    # 2.调用统计方法
    stack = deque([(root,0)])
    match way:
        case "type":
            print("按后缀名统计：")
        case "time":
            print("按修改时间统计：")
        case "mime":
            print("按mime类型统计：")

    for key,val in file_dict.items():
        size = math.ceil(val / 1024)
        print(f"{key}：{size}KB")
    pass


if __name__ == '__main__':
    arg_parse = cli_input_arg()
    args = arg_parse.parse_args()

    print(args)
    # 1.遍历对应文件夹
    traverse_content(args.root_path,args.recursive,False)






