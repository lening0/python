"""
字符串相关的工具模块
"""

def str_reverse(s):
    """
    字符串完成反转
    :param s:将被反转的字符串
    :return:反转后的字符串
    """
    return s[::-1]

def substr(s,x,y):
    """
    给定的下标完成切片
    :param s:被切片的字符串
    :param x:被切片的开始下标
    :param y:被切片的结束下标
    :return:切好片的字符串
    """
    return s[x:y]


if __name__ == '__main__':
    print(str_reverse("我是梓神"))
    print(substr("我是炫神",2,4))










