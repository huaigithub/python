#!/usr/bin/python
#coding=utf-8

#lambda 表达式测试
func = lambda x,y : x+y
print (func(2,3))


#函数可以当参数使用
def test(f, a, b):
	print(f(a, b))

test(func, 10, 20)

test((lambda x,y : x*3 + y), 7, 9)


#map 函数
re = map((lambda x:x+3), [1,2,3])
print(list(re))

re2 = map((lambda x,y :x+y), [1,2,3],[4,5,6])
print(list(re2))


#filter 函数
def func(a):
	if a>=100:
		return True
	else:
		return False
print(list(filter(func,[2,50,100,200,300])))
