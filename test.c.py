# name = ["li","li2","li3"]
#
# print(name)
#
# #print(type(name))
#
# name2 = [name,267,['pad',5]]
# #print(name2)
#
# print(name2[0][-1])
#
# print("hello world")
from os import replace

# my_list = ["hello world","hello chaina","hello python"]
#
# index = my_list.index("hello python")
# # print(index)
#
# my_list[1] = 666,"开paty不带我"
# my_list.insert(1,'oo的ye')
# print(my_list[1])
# print(my_list)
# b = [1.1,2]
# my_list = [1,2,3]
# my_list.append(b)
# print(my_list)


# a = [1,[1,3,9],2,[1,2,3]]
# # b = del a [2][2]
# # b = a.insert(2,6)
# # b=a.pop(2)
# # a.remove([1,3,9])
# # b = a.count([1,3,9])
# # print(b)
# # a.clear()
# # a.append(1)
# # c = a.count()
# # print(c)
# # b = print(b)
# b = len(a)
# print(b)
# a.clear()
# b = len(a)
# print(b)

# all_age = [21,25,21,23,22,20]
# all_age.append(31)
# all_age.extend([29,33,30])
# all_age.pop(0)
# all_age.pop(8)
# a = all_age.index(31)
# print(all_age)
# print(a)

# def list_while():
#       my_list = ["wo","shi","ni","die"]
#
#       index = 0
#       while index < len(my_list):
#           element = my_list[index]
#           print(f"列表的元素为{element}")
#           index+=1
#
# list_while()
#
# def list_for():
#     my_list = [1,2,3,4,5]
#     for elemnet in my_list:
#         print(elemnet)
#
#
# list_for()


# t1 = (1,"hello",True)
# t2 = (1,[1,2],2,2,3)
# t3 = tuple()
# print(f"t1的类型是{type(t1)},t1的内容是{t1}")
# print(f"t2的类型是{type(t2)},t2的内容是{t2}")
# print(f"t3的类型是{type(t3)},t3的内容是{t3}")
# t4 = (t2,)
# index = t2.index(2)
# print(index)
# print(t4)
# print(type(t4))
# num = t2.count(2)
# print(num)
#
# num1 = len(t2)
# print(num1)
# a = 0
# while a < len(t2):
#     print(t2[a])
#     a+=1
# for a in t2:
#     print(a)
# t2[1][1] = 3
# print(t2)
# name = ("周杰伦")
# age = (11)
# favourite = (["football","music"])
# yuanzu = (name,age,favourite)
# print(yuanzu)
#
# index = yuanzu.index(age)
# print(index)
#
# print(name)
#
# yuanzu[2][0] = 'coding'
# print(yuanzu)


# name = 'wo shi ni die'
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[-1])
#
# # name1[0] = 'W'
# num = index = name.index('ni')
# print(name[5])
# print(num)
# name1 = name.replace('shi','sho')
# print(name1)
# my_str = 12,'s o l','m','p'
# print(my_str)
# print(type(my_str))
#
# o = [1,2]
# print(type(o))
# my_str = "12,'s o l','m','p'"
#
# o = "adawdokdlkd"
# # print(type(o))
# o_list = o.split('d')
# print(o_list)

# o = "awpod wada          "
# print(o.strip(" "))

# o = "adaw dokd lkd"

# count = o.count('a')
# print(count)
# len = len(o)
# print(len)

# p = o.split()
# print(p)
# o = 'wo niu bi'
# count = 0
# while count < len(o):
#     print(o[count])
#     count+=1
#
# for num in o:
#     print(num)

# my_str = 'wo zhen shi fule'
# count = my_str.count("s")
# print(count)
# replace = my_str.replace(" ","|")
# print(replace)
# split = replace.split("|")
# print(split)
    #0 1 2 3 4
# o = [1,2,3,4,5]
# new_o = o[1:3:1]
# print(new_o)

# a = 'mn,pn,ln,on'
# split = a.split(",")
# new = split[2]
# new1 = new[::-1]
# print(new1)
# new_a = a[ ; -1]


# a = set()
# b = {"w",1,6,True}
# # b.add(6)
# # b.remove(1)
# # print(type(b))
# # print(b.pop())
# # print(b)
# # b.clear()
# # print(b)
# a = {'p',2,1,6,3}
# c = b.difference(a)
# d = b.union(a)
# b.difference_update(a)
# print(d)
# print(len(d))
#
# for i in d:
#     print(i)
# my_list = {'oo','dy','oo','dy',"李","宁","李","宁"}
# kong = set()
#
# for i in my_list:
#     kong.add(i)
# print(kong)

# my_dict1 = {"cxk":100,"lxn":0}
# my_dict2 = {}
# my_dict3 = dict()
# print(my_dict1)
# print(my_dict2)
# print(my_dict3)
# print(type(my_dict1))
# print(type(my_dict2))
# print(type(my_dict3))
# score = my_dict1['cxk']
# print(score)
# cxk = {"语文":100,"数学":100,"英语":100}
# lxn = {"语文":0,"数学":0,"英语":-1}
# chengji = {"cxk":cxk,"lxn":lxn}
# print(chengji)
# print(chengji['cxk']['语文'])
# chengji['lxn']['政治']=1
# print(chengji['lxn']['政治'])
# # cxk.remove("语文")
# # print(zuobifen)
#
# print(cxk)
# cxk = {"语文":100,"数学":100,"英语":100}
# keys = cxk.keys()
# # print(keys)
#
# for key in keys:
#     print(f"成绩科目为{key}",end = ' ')
#     print(f"科目分数为{cxk[key]}")
# for key in cxk:
#     print(f"科目为{key},分数为{cxk[key]}",end = print())
#
# num = len(cxk)
# print(num)

# info_dict = {
#     "wlh":{
#         "部门":"科技部",
#         "工资":3000,
#         "级别":1
#     },
#     "zjl":{
#         "部门":"市场部",
#         "工资":5000,
#         "级别":2
#     },
#     "ljj":{
#         "部门": "市场部",
#         "工资": 7000,
#         "级别": 3
#     },
#     "zxy":{
#         "部门": "科技部",
#         "工资": 4000,
#         "级别": 1
#     },
#     "ldh":{
#         "部门":"市场部",
#         "工资":6000,
#         "级别":2
#     }
# }
# print(f"员工信息为{info_dict}")
# for name in info_dict:
#     if info_dict[name]["级别"] == 1:
#         info_dict[name]["级别"] +=1
#         info_dict[name]["工资"] +=1000
# print(f"员工加薪后{info_dict}")
# my_list = [1,2,9,8,5,7,6]
# # print(set(my_list))
# print(sorted(my_list,reverse=True))

# def a(x,y=2,z=2):
#     print(x,y,z)
# a(x=2)

# def info(*args):
#     print(args)
# info("a:1",2,9)
#
# def infp(**kwargs):
#     print(kwargs)
# infp(name="xiaowang",n=1)
# def ooy(add):
#     num = add(1,2)
#     print(num)
# def ooy():
#     return "1,2"
# def add(ooy):
#     return ooy(x+y)
# add(ooy)
# def ee(a):
#     num = a(1,2)
#     print(num)
# ee(lambda x,y:x+y)













































































































