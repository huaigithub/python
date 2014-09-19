#--*-- encoding=utf-8 --*--
#!/usr/bin/python
__author__ = 'yangh'

def printInfo(num):
    print('**********************************************   %d   ***********************************************' % num)

ary = []
ary.append("a")
ary.append("b")
ary.append("c")

#len方法
print len(ary)

#count方法
print ary.count("a")
print ary.count("z")

#insert方法
ary.insert(2,"wwwwwww")

print ("this index is :%s" % ary.index("b",1,3))

#pop方法
print ary.pop(2)
print ary

#reverse方法
ary.reverse()
print ary

aryb = []
aryb.append("1")
aryb.append("2")
aryb.append("3")

#extend方法
ary.extend(aryb)
print ary

print "the second element is : %s " % ary[2]

for v in ary :
    print v

printInfo(1)
aryInt = [1,2,3,4,5,6,7,8,9,10]
print aryInt[7:10]
print aryInt[-3:0]
print aryInt[-3:-1]
print aryInt[-3:]
print aryInt[:3]

printInfo(2)
aryInt2 = [1,2,3,4,5,6,7,8,9,10]
print aryInt2[:10:1]
print aryInt2[:10:2]
print aryInt2[:10:3]
print aryInt2[1:10:2]
print aryInt2[::4]

print aryInt2[1:7:-1]
print aryInt2[10:1:-1]
print aryInt2[10:0:-1]
print aryInt2[10::-1]

printInfo(3)
aryInt3 = [1,2,3,4,5]
aryInt4 = [6,7,8,9,10]
print aryInt3 + aryInt4
str01 = "hello "
str02 = "python"
print str01 + str02

#print aryInt3 + str01 #出错，类型不一致

printInfo(4)

str03 = 'python '
print str03 * 5

printInfo(5)
ary001 = [50]
print ary001*5
print ['a'] * 10
print [None] * 10

printInfo(6)

str04 = 'python'
print 'py' in str04
ary002 = ['a','bc','de','fg','h']
print 'bc' in ary002

printInfo(7)
ary003 = [['abc','egf'],['hijk','lmn']]
print 'hijk' in ary003
print ['abc','egf'] in ary003

printInfo(8)
ary004=[231,86,5,36,56,9856]
print len(ary004)
print min(ary004)
print max(ary004)

printInfo(9)
str05 = 'abcdefg'
print len(str05)
print min(str05)
print max(str05)

printInfo(9)
ary005 = [['abc','egf'],['hijk','lmn']]
print len(ary005)
print min(ary005)
print max(ary005)

printInfo(10)
ary006 = ['a','b','c','x','y','z']
print ''.join(ary006)

printInfo(11)
str06 = 'abcdef'
ary007 = ['a','b','c','x','y','z']
#del str06[2] #错误的使用方式，字符串是不可以被这样删除的
del ary007[2]
print ary007

printInfo(12)
lst01 = list('abcdefg')
lst02 = list('123')
lst03 = list('123')
print lst01
lst01[1:]=list('123456789')
lst02[1:] = ['abcd'] #看看这样做是啥样的结果
lst03[1:] = ['a','b','c','d'] #看看这样做是啥样的结果
print  lst01
print  lst02
print  lst03

del lst03[1:3]
print lst03

printInfo(14)
ary008 = ['a','b','c',['a','c'],['b',['b','a']]]
print ary008.count('a')

printInfo(15)
ary009 = ['1','2','3']
ary010 = ['4','5','6']
ary009.extend(ary010)
print ary009



