# python的字符串用法

str = "hello, python!"
# python字符串运算符 "in" and "not in"
if 'h' in str:
    print("YES")
else:
    print("NO")
if 'k' in str:
    print("YES")
else:
    print("NO")

# python 字符串格式化符号 %c %s %d %f
print("%c %s %d %f" % ('a', "hello", 12, 12.3))  # a hello 12 12.300000

# python 三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)

#  f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去，
print(f"{2**7}")
