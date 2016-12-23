# -*- coding: UTF-8 -*-

### 高级特性

## 切片
# 切片操作符用来取指定索引范围的操作
# L[0:3]表示,从索引0开始取,到索引3停止,但不包括索引3,即索引0,1,2.如果第一个索引是0还可以省略为L[:3]
L = ['Sakura', 'Mikasa', 'Asuna', 'Misaki', 'Zou']
print L[0:3]     # ['Sakura', 'Mikasa', 'Asuna']
# 同样可以倒数切片,倒数第一个元素的索引是-1
print L[-2:]     # ['Misaki', 'Zou']
print L[-3:-1]   # ['Asuna', 'Misaki']

# 创建一个0-99的数列
L1 = range(100)      # [0, 1, 2, 3, 4, ......, 99]
# 前10个数,每两个取一个
print L1[0:10:2]     # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# 所有数,每10个取一个
print L1[::10]       # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# 如果什么都不写,只有一个 : 符号,就可以原样复制一个list
print L1[:]          # [0, 1, 2, 3, 4, ......, 99]

# 字符串'xxxx'也可以看成是一种list,每个元素就是一个字符,可以进行切片操作
L2 = 'ABCDEFGHI'
print L2[:4]      # 'ABCD'
print L2[::3]     # 'ADG'

## 迭代
# 通过for循环来遍历一个给定的list或tuple称为迭代
# Python的for循环不仅可以用在list或tuple,还可以用在其他可迭代对象上
# 因为dict的储存不是按照list 的方式顺序排列,所以,迭代出的结果可能不一样
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key      # a c b
# 迭代value
for value in d.itervalues():
    print value    # 1 3 2
# 迭代key和value
for k, v in d.iteritems():
    print k, v     # a 1  c 3  b 2

# 通过collections模块的Iterable可以判断一个对象是否是可迭代对象
from collections import Iterable
print isinstance('abc', Iterable)        # True
print isinstance([1, 2, 3], Iterable)    # True
print isinstance(123, Iterable)          # False

# enumerate()函数可以把一个list变成索引-元素对,这样可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print i, value    # 0 A   1 B   2 C

## 列表生成式

# 生成1-10的list
print range(1, 11)     # [1, 2, 3, ....., 9, 10]
# 生成[1*1, 2*2, 3*3, ...., 9*9, 10*10]的list
# 写列表生成式时,把要生成的元素x*x放在前面,后面跟for循环就可以创建list
print [x * x for x in range(1, 11)]     # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for循环后面还可以加上if判断,下述代码利用if判断筛选出仅偶数的平方
print [x * x for x in range(1, 11) if x % 2 == 0]     # [4, 16, 36, 64, 100]
# 使用两层循环生成全排列
print [m + n for m in 'ABC' for n in 'XYZ']   # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
# 列出当前目录下的所有文件和目录名
# ['.git', '.idea', 'README.md', 'test.py', 'test2.py', 'test3.py', 'test4.py', 'test5.py']
import os     # 导入os模块
print [d for d in os.listdir('.')]    # os.listdir可以累出文件和目录
# 列表生成式可以使用两个变量来生成list
j = {'x': 'A', 'y': 'B', 'z': 'C'}
print [k + '=' + v for k, v in j.iteritems()]    # ['y=B', 'x=A', 'z=C']
# 把list中所有的字符串变成小写
J1 = ['SAKURA', 'ASUNA', 'MIKASA']
print [s.lower() for s in J1]      # ['sakura', 'asuna', 'mikasa']
# 当list中包含字符串和整数时,需要通过if判断
J2 = ['SAKURA', 'ASUNA', 18, 'MIKASA']
print [s.lower() for s in J2 if isinstance(s, str) == True ]  # ['sakura', 'asuna', 'mikasa']
# 如果需要保留数字
print [s.lower() if isinstance(s, str) else s for s in J2]

## 生成器
# 创建一个生成器(generator),最简单的只需要把列表生成式的[]改成()
g = (x * x for x in range(1, 11))
print g       # <generator object <genexpr> at 0x025550A8>
# generator的next()方法可以一个一个的打印generator内的元素
print g.next()     # 1
print g.next()     # 4
print g.next()     # 9
# 因为generator是可迭代对象,所以可以通过for循环直接调用
for n in g:
    print n
