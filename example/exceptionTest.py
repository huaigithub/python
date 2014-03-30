#!/usr/bin/python
#coding=utf-8

lst = [1,2,3,4,5,6,7]

it = iter(lst)

try:
	for i in range(100):
		print(it.__next__())
except StopIteration:
	print("Error..............here is end", i)
finally:
	print("..........finally.............")



for x in range(100):
	print(it.__next__())
raise StopIteration
