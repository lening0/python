from sys import exception

import my_module
import my_utils.str_util
# print(type(f))

# print(f"读取20个字节的结果为{f.read(0)}")

# print(f.readline())
#
#
#
#
# print(f.readlines())
# for line in f:
#     print(line)

# f.close

# with open("d:/测试.txt",'r',encoding = "UTF-8")as f:
# print(f.read().count("print"))


# f = open("d:/测试.txt",'w',encoding = "UTF-8")
#
# f.write("萱萱的狗\n")
# # f.flush()
# f.close()
#
# f = open("d:/测试.txt",'a',encoding = "UTF-8")
# f.write("欧欧的耶\n")
# f.write("欧欧的耶")
# f.flush()
# f.close()
#
# f = open("d:/测试.txt",'r',encoding = "UTF-8")
#
# print(f.read())

# try:
#     f = open("D:/abc.txt", "r", encoding='UTF-8')
# except:
#     print("出现异常，文件不存在，我将open转化为'w'模式")
#     f = open("D:/abc.txt", "w", encoding='UTF-8')
# try:
#     print(name)
#     1/0
# except(NameError,ZeroDivisionError) as e:
#     print("没定义啊老弟")
#     print("没学过数学吗？除数为0也是神人了")
#     print(e)
#
# print(name)
# 1/0


# try:
#     # 1/0
#     # print(name)
#     # f = open("D:/abc","r")
# # except (NameError,ZeroDivisionError) as e:
# #     print("出现了未定义或除0异常")
#       print("hello")
#
# except Exception as e:
#     print("总之你出错了")
# else:
#     print("好高兴没有异常")
# finally:
#     print("辛苦了")

# def func1():
#     print("kaishi")
#     1/0
#     print("jieshu")
#
# def func2():
#     print("kaishi")
#     func1()
#     print("jieshu")
#
# def main():
#     print("kaishi")
#     try:
#         func2()
#     except Exception as e:
#         print(f"出现异常了，异常是{e}")
#
#
# main()

# import time
# from time import sleep


#
# from time import *
#
# print("hello")
# sleep(5)
# print("hello")

# import time as t
# t.sleep(3)
#
# from time import sleep as t
# t(5)

# from my_module import ADD as AD
# AD(3,6)
# from  my_module import *
# ADD(1,2)
# add(1,2)

# import my_package.my_module1
# from my_package.my_module1 import ADD as AD
# from my_package import *
# my_module1.ADD(1,2)
# import my_utils.str_util
# from my_utils import *
# print(my_utils.str_util.str_reverse("哦哦的耶"))
# print(my_utils.str_util.substr("wo niu bi",3,7))
import my_utils.str_util
from my_utils import file_util
# my_utils.str_util.str_reverse()

file_util.print_file_info("d:/测试.txt")
file_util.append_to_file("d:/测试.txt","bin哥不牛逼")






































