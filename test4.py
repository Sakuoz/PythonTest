# -*- coding: UTF-8 -*-

### 函数

## 调用函数

# 函数abs()可以求绝对值
# 调用函数时,如果传入的参数数量不对,或者传入的参数类型不对,会报错
print abs(100)      # 100
print abs(-2)       # 2

# 比较函数cmp(x, y),如果x < y,返回-1,如果x == y,返回0,如果x > y,返回1
print cmp(1, 2)     # -1
print cmp(1, 1)     # 0
print cmp(1, -1)    # 1


## 数据类型转换
# int()可以把其他数据类型转换为整数
print int(12.33)    # 12
print int('123')    # 123
# float()可以把一个字符串或一个整数转换为浮点数
print float('12')   # 12.0
# str()可以返回一个字符串
print str(1.23)     # '1.23'
# bool(x)将x转换为boolean(布尔值)类型,如果x缺省,返回False
print bool(1)       # True
print bool('')      # False

# 函数名其实就是指向一个函数对象的引用,完全可以把函数名赋给一个变量
a = abs
print a(-1)         # 1


## 定义函数
# 定义一个函数要使用def语句,依次写出函数名,括号,括号中的参数和冒号:,然后在缩进块中编写函数体,
# 函数的返回值用return语句返回
# 函数体内部的语句在执行时,一旦执行到return时,函数就执行完毕,并将结果返回
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print my_abs(-5)     # 5

# pass语句用来定义一个什么事也不做的空函数,可以用来做占位符
def nop():
    pass

# 参数检查
# 调用函数是,如果参数个数不对,解释器会报错,如果参数类型不对同样会报错
# my_abs('A')       # 'A'  因为my_abs没有进行参数检查
# abs('A')          # TypeError
# 内置函数isinstance可以进行数据检查
def new_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# print new_abs('A')   # 报错,因为A不属于整数或者浮点数


## 函数的参数

# 默认参数

# 在power函数中,n = 2即为默认参数,即使不输入n的值,函数也不会报错,而是使用默认的2进行计算,这样就可以计算x的n次方
# 必选参数必须在前,默认参数在后,否则python解释器会报错
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 默认参数必须指向不变对象,可以用None这个不变对象实现