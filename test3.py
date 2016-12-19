# -*- coding: UTF-8 -*-

### 使用dict和set

## dict

# dict使用键-值(key-value)存储,具有极快的查找速度
# list为中括号[], tuple为小括号(), dict使用的是大括号
d = {'Sakura': 95, 'Mikasa': 80, 'Asuna': 75}
print d['Sakura']  # 95

# 把数据放入dict的方法,除了初始化时指定,还可以通过key放入
# 一个key只能对应一个value,多次对一个key放入value,后面的值会把前面的值覆盖
d['Misaki'] = 89
print d['Misaki']    # 89
d['Misaki'] = 77
print d['Misaki']    # 77

# 如果key不存在,dict就会报错
# d['Tom']     # 报错,因为dict d中没有Tom这个key值
# 通过in可以判断key是否存在
print 'Tom' in d    # False
# 或者通过dict提供的get()方法,如果key不存在,可以返回None,或者自己指定的value
print d.get('Tom', -1)

# pop(key)方法可以删除key值,对应的value也会从dict中删除
# dict内部存放的顺序和key放入的顺序是没有关系的
# dict的key必须是不可变对象
print d
d.pop('Misaki')
print d


## set

# set和dict类似,也是一组key的集合,但不存储value,在set中没有重复的key
# set和dict唯一的区别仅在于没有存储对应的value值,原理是相同的,所以不能放入可变对象
# 要创建一个set,需要提供一个list作为输入集合
s = set([1, 2, 3])
print s     # set([1, 2, 3])
# 重复元素在set中被自动过滤
x = set([1, 2, 2, 3, 3])
print x     # set([1, 2, 3])

# 可以使用add(key)方法添加元素到set中,可以重复添加,但不会有效果
s.add(4)
print s     # set([1, 2, 3, 4])
# 通过remove(key)方法可以删除元素
s.remove(3)
print s     # set([1, 2, 4])

# 两个set可以做数学意义上的交集,并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2     # set([2, 3])
print s1 | s2     # set([1, 2, 3, 4])
