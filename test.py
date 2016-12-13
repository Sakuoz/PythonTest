# -*- coding: utf-8 -*-

# 变量
my_name = 'Mr.Zou'
my_height = 178
my_weight = round(90.2222)
a = 'A'
n = 'n'
g = 'g'
e = 'e'
l = 'l'

print 'my height is', my_height, 'cm.'
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print 'my weight is %s kg.' % my_weight
print 'my weight is %d kg and my name is %s' % (my_weight, my_name)
print '1' * 10
print a + n + g + e + l
print 'hello world!'

# 变量名要以字母开头
# round()函数可以使浮点数四舍五入
# %s, %d, %r是一种'格式控制工具'.它们告诉Python把右边的变量带到字符串中,并且把变量的值放到%s所在的位置
# $r用来调试最好,它会显示变量的原始数据,$s和其他符号则是用来向用户显示输出的
# $d 整数, $f浮点数, $s字符串, %x十六进制整数

# list 和 tuple
classmates = ['Mike', 'Sakura', 'Mikasa']
print classmates
print len(classmates) # 3
print classmates[0]   # Mike
print classmates[1]   # Sakura
print classmates[-1]  # Mikasa
print classmates[-2]  # Sakura
classmates.append('adam')
print classmates
# list是一个有序的集合,变量classmates就是一个list,list是一个可变的有序表,所以可以在list末尾追加元素
# len()函数可以获得list元素的个数
# 索引是从0开始,索引-1可以直接获取最后一个元素
