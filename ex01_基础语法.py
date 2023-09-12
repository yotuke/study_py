"""
python基础语法
    1.注释
        单行注释：   # 第一个注释
        多行注释：   ''' 第二个注释   '''
        多行注释    ‘’‘’‘’ 第三个注释  ‘’‘’‘’
    2.多行语句
        语句过长可以使用反斜杠来实现换行
        total = item_one + \
                item_two + \
                item_three
    3.数字类型（Number）类型
        1.int(整数)
        2.bool(布尔)
        3.float(浮点数)
        4.complex(复数)：1+2j
    4.字符串（String）
        1.python中的单引号和双引号完全等价
        2.使用 r"this is a line " 可以使双引号中的字符串不转义，原样输出
    5.print输出
        print输出是默认换行的，如果不需要换行在变量末尾加上 end=""
"""
s = "hello, world!"
print(s, end="")
