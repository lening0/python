"""
文件处理相关的工具模块
"""
from errno import ENAMETOOLONG


def print_file_info(file_name):
    """
    功能:将给定路径的文件内容输出到控制台中
    :param file_name:
    :return:None
    """
    f = None
    try:
        f = open(file_name,"r",encoding = "UTF-8")
        content = f.read()
        print("所有文件如下")
        print(content)
    except Exception as e:
        print(f"出错，原因为{e}")
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    print_file_info("d:/测试.txt")

def append_to_file(file_name,data):
    """
    将指定数据存到指定文件
    :param file_name:指定文件
    :param data: 制定数据
    :return: None
    """
    f = open(file_name,"a",encoding="UTF-8")
    f.write("\n")
    f.write(data)
    f.write("\n")
    f.close()



if __name__ == '__main__':
    append_to_file("d:/测试.txt","bin哥你骗人呢")









