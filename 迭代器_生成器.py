#!/usr/bin/python
# -*- coding: utf-8 -*-
print ('第一个例子，用列表生成式生成列表')
print ('列表生成式的语法 [x for x in range(1,6)]')#注意和后面的生成器的语法作对比


list1=[x*x for x in range(1,6)]
list1
print (list1)



#比如返回1～6之间个数的平方，通过循环来解

print ('用for循环解决')
for x in range(1,6):
	print (x*x)	#用print实现

print ('用for循环列表打印 ')
nums=[]
for num in range(1,6):
	y=num*num
	nums.append(y)
print (nums)


#下面是迭代器内容
print ('下面是迭代器内容')
print ('迭代器概念约束理解')
print('一、简而言之就是一句话：如果一个对象包括一个叫"next"(python3 为__next__)的方法，那么这个对象就叫做“迭代器”。')
#简而言之就是一句话：如果一个对象包括一个叫"next"(python3 为__next__)的方法，那么这个对象就叫做“迭代器”。

print ('二、为了使用这个for..in 迭代语法糖，我们需要在in后面放可以迭代的“迭代器”,通常来讲，当我们要创建了一个迭代器时，我们还“必须”(注意是必须)让迭代器可迭代\n可迭代协议\n1，这个迭代器必须同时包含另一个方法叫做“__iter__” \n2，这个"__iter__"方法还得返回一个”迭代器“')


class Counter:
    def __init__(self):
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        i = self.index
        if i < 10:
            self.index += 1
            return i
        else:
            raise StopIteration

counter = Counter()
for i in counter:
    print (i)





print ('在python中，我们可以使用"iter"这个函数来返回一个“可迭代的迭代器”。')

x = iter([1, 2, 3])
print(x) 	#<list_iterator object at 0x10c828550>
next(x)   # 返回 1
next(x) # 返回 2
next(x) # 返回 3




print ('也可让一个普通对象可迭代')

class Name:
    def __iter__(self):
        return iter(['zhangsan', 'lisi', 'wangwu'])

name = Name()
for n in name:
    print(n)


#下面是生成器部分
print ('下面是生成器部分\n生成器返回的是一个迭代器，有两种语法\n一、（x for x in range(start,)end）\n二、正常代码含yield关键字')
print ('第一种方法实例')
g1=(x*x for x in  range(1,6))	#g1为一个迭代器
print('直接返回g1看看')
print (g1)
print ('返回迭代器结果')
for x in g1:
	print (x)


print ('第二种方法实例')
def sequare(start,end):
	for x in range(start,end):
		yield x*x

g2=sequare(1,6)
print('直接返回g2看看')
print (g2)
print ('返回迭代器结果')
for x in g2:
	print (x)


