# -*- coding: UTF-8 -*-


### 条件判断和循环

## 条件判断

age = 20
if age >= 18:
    print 'your age is', age
    print 'adult'
elif age >= 12:
    print 'your age is', age
    print 'teenager'
else:
    print 'your age is', age
    print 'kid'

# if是从上往下判断的,如果在某个判断上是true,下面的判断就不会执行
# elif 是else if的缩写,完全可以有多个elif,所以if语句的完整形式是:
# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>

## 循环

names = ['Mike', 'Sakura', 'Mikasa']
for name in names:
    print name
# 这段代码会依次打印names的每一个元素,所以 for x in ...循环就是把每个元素带入变量x,然后执行缩进块的语句

sum = 0
for x in range(101):
    sum = sum + x
print sum
# range()函数可以生成一个整数序列,比如range(5)生成的序列是从0开始小于5的整数[0, 1, 2, 3, 4]
# 所以可以用上述代码来求1-100的整数和

num = 0
n = 99
while n > 0:
    num = num + n
    n = n - 2
print num


birth = int(raw_input('birth: '))
if birth < 2000:
    print '00前'
else:
    print '00后'
