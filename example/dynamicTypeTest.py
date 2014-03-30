#!/usr/bin/python
#coding=utf-8

a=3
print(a, type(a))
a = "hello word"
print(a, type(a))

print("---------------------------------------------------------------")
L1 = [1,2,3]
print(L1)
L2 = L1
print(L2)
L1 = 1
print(L1)
print(L2)

print("---------------------------------------------------------------")
def f(x):
    x = 100
    print(x)

a = 1
f(a)
print(a)