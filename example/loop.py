#!/usr/bin/python
#coding=utf8

s1 = (1,2,3,4,5,6,7,8,9,10)
s2 = [10,9,8,7,6,5,4,3,2,1]

for x in s1:
	print(x)
print("------------------------------------1-------------------------------------")
for y in s2:
	print(y)

print("------------------------------------2-------------------------------------")

idx = range(5)
for z in idx:
	print(z)
print("------------------------------------3-------------------------------------")

i = 0
while i < 10:
    print(i)
    i = i + 1
print("------------------------------------4-------------------------------------")

for a in range(10):
    if a == 2: 
        continue
    print(a)
print("------------------------------------5-------------------------------------")

for b in range(10):
    if b == 2:        
        break
    print(b)