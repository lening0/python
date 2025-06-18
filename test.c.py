# print("请输入密码")

# password = input("请输入密码")
#
# print("你的密码为%s" % password)


# num = int(num)

# password = input("请输入密码")
# password = int(password)
# print(type(password))

# bool_1 = 7>6
# bool_2 = type(bool_1)
# print(f"7>6的结果为：{bool_1},类型是{bool_2}")

# num1 = 10
# num2 = 10
# print(f"num和num2的结果为{num1 == num2}")

# num1 = 10
# num2 = 15
# print(f"num1和num2不相等为{num1 != num2}")

# name1 = "it"
# name2 = "io"
# print(f"name1 和 name2是否相等{name1 == name2}")
#
#
#
# num1 = 10
# num2 = 15
# print(f"10>=15为{num1>num2}")
# print(f"10<=15为{num1<num2}

# age = 10
# print(f"我已经{age}岁了")
# if age >= 18:
#     print("我成年了")
#     print("时间过的真快")
#
# print("我该上大学")
# print("aodjpao")
# if age <18:
#     print("未成年")

# if 7>3:
    # print("niubi")

# age = int(input(f"""
# 欢迎来到游乐园，儿童免费，成人收费。
# 请输入你的年龄:"""))
# if age >= 18:
#     print("交钱")
#
# # if age < 18:
# else:
#     print("随便玩不交钱")
# print("祝您游玩愉快")

# print("欢迎来到游乐园")
# height = int(input("请输入你的身高"))
# huiyuan = input(f"有无会员？")
# age = int(input("年龄为："))
# if height < 150:
#     print("随便玩小矮子")
# elif huiyuan == "有":
#     print("玩去吧富哥")
# elif age <= 18:
#     print("玩去吧小屁孩")
# else:
#     print("给钱，10块")

# if int(input("请输入你的身高（cm）：")) < 120:
#     print("进去吧矮子")
# elif int(input("请输入你的vip：")) > 5:
#     print("进去吧富哥")
# else:
#     print("给钱")
# print("祝您游玩愉快")

# really_num = 5
# if int(input("请输入第一次猜想的数字:")) == really_num:
#     print("猜对了")
# elif int(input("请输入第二次猜想的数字:")) == really_num:
#     print("猜对了")
# elif int(input("请输入第三次猜想的数字:")) == really_num:
#     print("猜对了")
# else:
#     print("菜就多练")
# print(type(really_num))


# print("欢迎参加高考")
# if input("请问你之前喜欢烫头吗") != "不喜欢":
#     print("喜欢烫头这辈子有了")
#     if input("小伙子谈过几次恋爱啊？") != "没谈过":
#         print("你个废物，不学习光谈恋爱了")
#         if input("小伙你觉得满分100分你能考多少？") == "100":
#             print("小伙有野心不错")
#             print("进去吧")
#         else:
#             print("干啥啥不行，给我滚")
#     else:
#         print("小伙不谈恋爱未来可期")
#         print("这几年做的不错可以进去了")
#
# else:
#     print("小伙不烫头未来有前途啊")
#     print("这几年做的不错可以进去了")

# import random
# num = random.randint(1,10)
# # print(num)
# guess_num = int(input("请输入你要猜的第1次数字"))
# if guess_num == num:
#     print("恭喜你猜中了")
# else:
#     if guess_num >num:
#         print("猜大了")
#     else:
#         print("猜小了")
#     guess_num = int(input("请输入你要猜的第2次数字"))
#     if guess_num == num:
#         print("恭喜你猜中了")
#     else:
#         if guess_num > num:
#             print("猜大了")
#         else:
#             print("猜小了")
#         guess_num = int(input("请输入你要猜的第3次数字"))
#         if guess_num == num:
#             print("恭喜你猜中了")
#         else:
#             print("三次不中回家种地去吧")
#             print(f"正确答案为{num}")

# i = 1
# while i <= 100:
#     print(f"lbw nb{i}次!")
#     i += 1

# sum = 0
# i = 1
# while i <=100:
#     sum += i
#     i += 1
#
# print(sum)


# while int(input("请猜数字1-100内")) != num:
#     elif int(input("请猜数字1-100内")) > num:
#         print("猜大了")
#     else:
#         print("猜小了")
# else int(input("请猜数字1-100内")) == num:
#         print("猜对了")
# if int(input("请猜数字1-100内")) == num:
#     print("猜对了")
# else:
#     while int(input("请猜数字1-100内")) != num:
#         if int(input("请猜数字1-100内")) > num:
#             print("猜大了")
#         else:
#             print("猜小了")
# import random
# num = random.randint(1,100)
# count = 0
# flag = True
# while flag:
#     guess_num = int(input("请输入你要猜的值"))
#     if guess_num == num:
#         print("恭喜你猜对了")
#         print(f"你一共猜了{count}次")
#         flag = False
#     else:
#         count +=1
#         if guess_num >num:
#             print("猜大了")
#         else:
#             print("猜小了")

# i = 1
# while i <= 100:
#     print(f"今天是第{i}天，准备表白......")
#     j = 1
#     while j <= 10:
#         print(f"我送出第{j}朵玫瑰花")
#         j += 1
#         print("小美我喜欢你")
#     i+=1
# print(f"坚持到第{i - 1}天，表白成功")


# print("hello",end="")
# print("hello")
# print("hello\tworld\ti\tam\tli")
# print("Life\tis\tshot\tyou\tneed\tpython")

# i = 0
# while i <= 9:
#     j = 1
#     while j<= i:
#         print(f"{i} * {j} = {i * j}",end='\t')
#         j+=1
#     i+=1
#     print()


# for x in "wo shi ni die":
#     print(x)
# count = 0
# for x in "wo shi ni die":
#     if x == "i":
#         count+=1
# print(count)

# for x in range(9):
#     print(x)
# for x in range(3,9):
#     print(x)
# for x in range(0,9,3):
#     print(x)

# for x in range(10):
#     print("送了一个飞机")

# count = 0
# for x in range(1,100):
#     if x % 2 == 0:
#         count += 1
# print(count)

# for i in range(1,101):
#     print(f"今天第{i}天")
#     for j in range(1,11):
#         print(f"这是今天送的第{j}束玫瑰花")
#     print("bb我爱你")
# print()
# print(f"在第{i}天bb接受了我的表白")

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j} * {i} = {i * j}", end = '\t')
#     print()


# for i in range(1,6):
#     print("1")
#     # continue
#     # break
#     # print('ad')
#     for j in range(1,6):
#         print('2')
#         break
#         print('3')
#     print('4')

# import random
# yue = 10000
# if yue:
#     for i in range(1,21):
#         num = random.randint(1, 10)
#         if num>= 5:
#             num-=1000
#             print(f"向员工{i}号发1000元工资，账户余额还剩{num}元")
#         else
# else:
#     print("工资发完了，下个月领取吧")

# import random
# yuan = 10000
# for i in range(1,21):
#     num = random.randint(1, 10)
#     if 1:
#         if yuan == 0:
#             print("工资发完了")
#             break
#         elif num < 5:
#             print(f"员工{i}号绩点为{num},不合格下一位")
#             continue
#         else:
#             yuan -= 1000
#             print(f"给{i}号发1k元，工资还剩{yuan}")
#             continue

# str1 = input("请输入你要测试的单词")
# def my_len(data):
#     count = 0
#     for i in data:
#         count+=1
#     print(f"一共{count}个字符")
# my_len(str1)


# def say_hi():
#     print("hi")
# say_hi()

# def add(a ,b):
#     """
#     代入值相加
#     :param a:相加的数字1
#     :param b:相加的数字2
#     :return:返回相加值
#     """
#     c = a+b
#     return c
#
# c = add(6,9)
# print(c)
# def switch(a):
#     if a > 37.5:
#         print("gun")
#     else:
#         print("jin")
# switch(1)

# def mo(a):
#     print("a")
# print(type(print(mo)))

# def po(a):
#     if a>18:
#         print("aaa")
#     else:
#         return None
#
# po(6)
# e = 10
# def a():
#     print("b")
# def b():
#     global e
#     e = 3
#     print(e)
#     print("a")
#     a()
#     print("c")
# b()
# print(e)


money = 5000000
name = None
name = input("name:")
def chaxun():
    print(f"""
    --------------余额查询-------------
    {name}你好，你就剩{money}元了，省着点花吧""")

def cunkuan(a):
    global money
    money += a
    print(f"""
    --------------存款-------------
    {name}你好，你都有{money}元了，多花点吧""")

def qukuan(a):
    global money
    money += a
    print(f"""
    --------------取款-------------
    {name}你好，你就有{money}元了，少花点吧""")

while 1:
        print(f""""
    -----------主菜单----------
    {name}你好，欢迎来到银行，请选择操作:
    查询余额输入1
    存款输入2
    取款输入3
    退出输入4""")
        xuanze = int(input("请输入你的选择"))

        if xuanze == 1:
            chaxun()
        elif xuanze == 2:
            cunkuan(int(input("存多少啊老弟？")))
        elif xuanze == 3:
            qukuan(int(input("取多少啊老弟？")))
        else:
          break












































































