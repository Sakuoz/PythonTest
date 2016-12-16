# -*- coding: utf-8 -*-

### 变量  

# 变量名要以字母开头
my_name = 'Mr.Zou'
my_height = 178
# round()函数可以使浮点数四舍五入
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

# %s, %d, %r是一种'格式控制工具'.它们告诉Python把右边的变量带到字符串中,并且把变量的值放到%s所在的位置
# $r用来调试最好,它会显示变量的原始数据,$s和其他符号则是用来向用户显示输出的
# $d 整数, $f浮点数, $s字符串, %x十六进制整数


### list 和 tuple

# list是一个有序的集合,变量classmates就是一个list,list是一个可变的有序表,所以可以在list末尾追加元素
classmates = ['Mike', 'Sakura', 'Mikasa']
print classmates
# len()函数可以获得list元素的个数
print len(classmates) # 3
# 索引是从0开始,索引-1可以直接获取最后一个元素
print classmates[0]   # Mike
print classmates[1]   # Sakura
print classmates[-1]  # Mikasa
print classmates[-2]  # Sakura
# append()函数可以追加元素到list末尾
classmates.append('Tom')
print classmates  # 'Mike', 'Sakura', 'Mikasa', 'Tom'
# pop()函数可以删除list末尾的元素,pop(i)可以删除指定的位置的元素,这里的i为索引位置
classmates.pop(2)
print classmates  # 'Mike', 'Sakura', 'Tom'
# 替换元素可以直接赋值给对应的索引位置
classmates[0] = 'Asuna'
print classmates  # 'Asuna', 'Sakura', 'Tom'

# tuple同样是一个有序列表,称为元组,tuple和list非常相似,但是tuple一但初始化就不可修改,其他获取元素的方法和list一致
# 定义tuple的方法为使用小括号(),而list使用的为中括号[]
# 当tuple中只有一个元素时不可定义为t = (1),因为括号()既可以表示tuple,又可以表示数学公式中的小括号,
# 因此当只有一个元素时需要加一个逗号','来消除歧义
t = (1)
print t  # 1
t = (1,)
print t  # 1,
