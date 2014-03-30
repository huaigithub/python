#!/usr/bin/python
#code = utf8

#序列有两种：tuple（定值表； 也有翻译为元组） 和 list (表)序列有两种：tuple（定值表； 也有翻译为元组） 和 list (表)

print("========================================1===================================")
s1=(1, 1.3, 'love', 5.6, 9, 12, False)
s2=[True, 5, 'smile']
print(s1, type(s1))
print(s2, type(s2))

#tuple和list的主要区别在于，一旦建立，tuple的各个元素不可再变更，而list的各个元素可以再变更。一个序列作为另一个序列的元素

s3 = [100, 200, s2]
print(s3)
s4 = [100, 200, [1000, 2000]]
print(s4)
s5 = []
print(s5)


print("========================================2===================================")
print(s1[0])
print(s2[2])
print(s3[2][0], s3[2][1], s3[2][2])

print("========================================3===================================")
s2[2] = 50000
print(s2)

print("========================================4===================================")
print(s1[:5])
print(s1[3:])
print(s1[0:7:3])

print("========================================5===================================")
s6 = (1,2,3,4,5,6,7,8,9,10)
print(s6[2:0:-1])

print("========================================6===================================")
print(s6[-1])
print(s6[-3])
print("========================================7===================================")
str = 'abcdef'
print(str[2:4])

#tuple元素不可变，list元素可变