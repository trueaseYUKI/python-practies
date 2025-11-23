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
    # 访问列表（判断是否已经访问过对应的路径）
    visit_list = set()
    while stack:
        # 从栈顶弹出（深度优先）
        root_path, depth = stack.pop()
        # 判断是否已经访问过改路径了
        resolve_path =  root_path.resolve()
        if resolve_path.__str__() in visit_list:
            # 访问过就直接进行下一次循环
            continue
        try:

            # 先打印当前目录信息
            modify_time = root_path.stat().st_mtime
            size = root_path.stat().st_size
            time_stamp = datetime.fromtimestamp(modify_time)
            format_time = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
            file_type = 'dir'
            name = root_path.name

            # 将对应的绝对路径加入到访问列表
            visit_list.add(resolve_path.__str__())
            print(f"{' '*(depth*2)}/{name:<20} {file_type:<10} {size:>8}B {format_time} {resolve_path.__str__()}")

            # 收集子目录，稍后压入栈中（保证正确的遍历顺序）
            subdirs = []

            # 遍历当前目录下的所有项目
            for item in root_path.iterdir():
                modify_time = item.stat().st_mtime
                size = item.stat().st_size
                time_stamp = datetime.fromtimestamp(modify_time)
                format_time = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
                name = item.name

                resolve_path = item.resolve()

                if item.is_file():
                    # 处理文件
                    file_type, encoding = mimetypes.guess_type(name)
                    if file_type is None:
                        file_type = item.suffix[1:] if item.suffix else 'unknown'

                    print(f"{'-'*(depth * 2)}{name:<20} {file_type:<10} {size:>8}B{ format_time} {resolve_path.__str__()}")
                elif item.is_symlink() and is_follow:
                    # 如果访问的是符号连接，并且对它选择允许跟随
                    # 1.判断它的真实路径是文件/文件夹
                    real_path = item.resolve()
                    # 处理符号链接
                    print(f"{'-' * (depth * 2)}{name:<20} {file_type:<10} {size:>8}B {format_time} {real_path.__str__()}")
                    if real_path.is_file():
                        print(f"{'-' * (depth * 2)}{name:<20} {file_type:<10} {size:>8}B {format_time} {real_path}")
                    elif real_path.is_dir() or real_path.is_symlink():
                        subdirs.append(real_path)
                    pass
                # 可能产生嵌套访问的根本在于文件夹，所以我们只要对文件夹进行判断即可
                elif item.is_dir():
                    # 收集子目录，后续统一处理
                    subdirs.append(item)


            # 将子目录按逆序压入栈中（保证正确的遍历顺序）
            for subdir in reversed(subdirs):
                # 如果已经访问过改文件，就直接跳过
                if subdir.resolve().__str__() in visit_list:
                    continue
                else:
                    # 将对应的绝对路径加入到访问列表中
                    stack.append((subdir, depth + 1))

            # 最后清空这个访问列表

        except Exception as e:
            print(f"scan root path find Error:{e}")
    visit_list.clear()
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
        # 深度优先遍历实现栈

        queue = deque([(current_path,0)])
        format_recursion_output(queue,is_follow=is_follow)
        pass
    else:
        for item in current_path.iterdir():
                # 1.生成FileInfo对象
                file_type = 'dir'
                size = item.stat().st_size
                # 这里要改为item而不是current_path
                modify_time = datetime.fromtimestamp(item.stat().st_mtime)
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

    pass



def sum_size(file_dict:dict,way:str,file:Path):
    key = None
    if way == "type":
        key = file.suffix[1:]
    elif way == "date":
        modify_time = datetime.fromtimestamp(file.stat().st_mtime)
        modify_date = modify_time.strftime("%Y-%m-%d")
        key = modify_date
    size = file.stat().st_size
    if key != None and key not in file_dict:
        file_dict[key] = size
    else:
        file_dict[key] += size

# statistics 模块
def statistics_file_size(file_dict:dict[str,float],queue:deque[Path],way:str):
   # 1.先判断根据什么统计（利用广度优先遍历BFS）
    while queue:
        # 出队
        root = queue.popleft()
        if root.is_file():
            sum_size(file_dict,way,root)
        # 如果是文件夹就扫描它
        elif root.is_dir():
            for item in root.iterdir():
                # 如果扫描到文件或文件夹就入队
                if item.is_file() or item.is_dir():
                    # 如果是链接文件就不入队
                    if item.is_symlink():
                        continue
                    else:
                        queue.append(item)

    pass



# 格式化统计结果
def format_statistics_result(root_path:str,way:Optional[str]):
    if(way == "None"): return


    file_dict = {}
    root = Path(root_path)
    queue = deque([root])
    statistics_file_size(file_dict, queue, way)

    # 标题
    match way:
        case "type":
            print(f"{'文件类型':<15} {'总大小':>10}")
        case "date":
            print(f"{'修改日期':<15} {'总大小':>10}")
        case "mime":
            print(f"{'MIME类型':<20} {'总大小':>10}")

    print("-" * 30)

    for key, val in file_dict.items():
        # 将字节转换为KB，四舍五入
        size_kb = math.ceil(val / 1024)
        print(f"{key:<20} {size_kb:>10} KB")

    pass


if __name__ == '__main__':
    arg_parse = cli_input_arg()
    args = arg_parse.parse_args()

    print(args)
    # 1.遍历对应文件夹
    traverse_content(args.root_path,args.recursive,args.follow)
    # 2.统计文件夹的文件大小
    format_statistics_result(args.root_path,args.statistics)






