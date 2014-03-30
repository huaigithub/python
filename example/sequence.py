#!/usr/bin/python
#code = utf8

#序列有两种：tuple（定值表； 也有翻译为元组） 和 list (表)序列有两种：tuple（定值表； 也有翻译为元组） 和 list (表)

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

