import argparse
import  logging
from datetime import datetime
from typing import Tuple, List
from pathlib import Path


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
        print(f"{item.name}\t{item.type}\t{item.size}B\t{item.update_time}\t{item.path}")
    pass

def format_recursion_output(path:Path,depth=1,previous=1):
    """
    格式化输出递归方式的文件夹访问
    :param path:
    :return:
    """
    for item in path.iterdir():

        modify_time = item.stat().st_mtime
        size = item.stat().st_size
        time_stamp = datetime.fromtimestamp(modify_time)
        format_time = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
        file_type = 'dir'
        name = item.name
        if item.is_file():
            # 1.如果是文件的话，就直接输出文件的信息
            file_type = 'file'
            print(f"{'-'*(depth**2)}{name}\t {file_type}\t {size}B\t {format_time}\t")
        elif item.is_dir():
            # 2.如果是文件夹就继续下去
            print(f"{'-'*(depth**2)}{name}\t {file_type}\t {size}B\t {format_time}\t")
            # 2.1.进行递归
            format_recursion_output(Path(item),depth+1,depth)

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
        format_recursion_output(current_path,depth=1,previous=0)
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
                    file_type = 'file'
                    pass
                file_info = FileInfo(item,item.name,file_type,size,formatted_time,1)
                # 加入到file_struct_list中
                file_structs.append(file_info)
        format_non_recursion_output(file_structs)
        pass
        # 3.2.显示当前文件夹的第一层的文件

    pass








if __name__ == '__main__':
    arg_parse = cli_input_arg()
    args = arg_parse.parse_args()
    # 1.遍历对应文件夹
    traverse_content(args.root_path,args.recursive,False)






