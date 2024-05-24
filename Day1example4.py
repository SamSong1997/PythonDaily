"""
变量的数据类型

"""

a = 123
b = 1.23
c = 'hello'
d = 2 > 3
e = 3 + 5j

# Ctrl+D = 复制代码
# Ctrl+Y = 删除代码

# int ---> integer （整数）整型
print(a, type(a))
# float (小数)浮点型
print(b, type(b))
# str ---> string （字符串）字符串型
print(c, type(c))
# bool ---> boolean 布尔型（True/false）（python的关键字、布尔值，表示真的假的，真的是True，假的是False）
print(d, type(d))
# complex（复数类型）
print(e, type(e))

# 变量可以重新赋值，对应类型也会发生变化
e = 'goodbye'
print(e, type(e))

