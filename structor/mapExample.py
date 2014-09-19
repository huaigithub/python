# -*- coding:utf-8 -*-
from copy import deepcopy


#字典数据结构
mapExmple = {}
mapExmple['name'] = 'my name'
mapExmple['age'] = 100
mapExmple['sex'] = 'men'
mapExmple['tmp'] = 'tmp'

print mapExmple
del mapExmple['tmp']
print mapExmple

print "-------------------------------1---------------------------------------"
print mapExmple.pop('name')
#print mapExmple.pop('name1') #报错
print mapExmple.pop('name1', 'i am default value!!!')

for k in mapExmple:
    print k

print "-------------------------------2---------------------------------------"
print mapExmple.get("name1")

print "-------------------------------3---------------------------------------"
print mapExmple.items()
items = mapExmple.items()
print "print items[1]" ,items[1]
print "print items[1][0]", items[1][0]
for item in items:
    print item

print "-------------------------------4---------------------------------------"
keys = mapExmple.iterkeys()
print "the keys dataType is:",type(keys)

for key in keys:
    print key
while 1:
    try:
        print keys.next()
    except Exception, e:
        break
print "-------------------------------5---------------------------------------"
print mapExmple.has_key("age")

print "-------------------------------6---------------------------------------"
mapkeys = mapExmple.keys()
print type(mapkeys)
print mapkeys

print "-------------------------------7---------------------------------------"


print "-------------------------------8---------------------------------------"
ary = [('name','xiaohong'),('age',10),('sex','men')]
aryDict = dict(ary)
print ary
print aryDict
print len(aryDict)
print "-------------------------------9---------------------------------------"
d = dict(name='xiaohong',age=10, sex='men')
print d

print "-------------------------------10---------------------------------------"
x=d.copy()
d['name'] = "hello i'"
d.clear()
print x




print "-------------------------------100---------------------------------------"

people = {
    'xiaoming':{
        'phone':'123',
        'addr':'Beijing'
     },
    'zhangsan':{
        'phone':'456',
        'addr':'shanghai'
    },
    'lisi':{
        'phone':'789',
        'addr':'guangzhou'
    }
}
print people
print people.get('xiaoming')
name='lisi'
key = 'addr'
labels={
    'phone':'phone namber',
    'addr' : 'address'
}
if name in people:
    print "%s's %s is %s ." % (name,labels[key], people[name][key])

print "---------------------------101-------------------------------------------"
template = "<html>" \
                "<head><title>%(title)s</title></head>" \
                "<body>" \
                    "<h1>%(title)s</h1>" \
                    "<p>%(text)s</p>"\
            "</body>"
data = {'title':'my home page', 'text':'Welcome to my home page!'}
print template % data


print "----------------------------102------------------------------------------"

mapExmple.clear()
print mapExmple

print "------------------------------103----------------------------------------"
map3 = {"name":'name1','age':10,'sex':'men'}
map4 = map3
print map3
map3.clear()
print map4
print "------------------------------103----------------------------------------"
map5 = {"name":'name1','age':10,'sex':'men'}
map6 = map5.copy()
print map5
print map6
map5['name']='aaaaaaaaaaabbbbb'
print map5
print map6

print "------------------------------104----------------------------------------"
map7 = {"name":'name1','age':10,'sex':'men'}
map8 = map7.copy()
print map7
print map8
map8['name']='aaaaaaaaaaabbbbb'
print map7
print map8

print "------------------------------105----------------------------------------"
map9 = {"name":'name1','age':10,'sex':'men','class':['a', 'b', 'c']}
map10 = map9.copy()
print map9
print map10
map10['class'].remove('b')
print map9
print map10


print "------------------------------106----------------------------------------"
map11 = {"name":'name1','age':10,'sex':'men','class':['a', 'b', 'c']}
map12 = deepcopy(map11)
print map11
print map12
map12['class'].remove('b')
print map11
print map12
print "------------------------------107----------------------------------------"
map13 = {"name":'name1','age':10,'sex':'men'}
iter = map13.iteritems()
print map13.items()
print iter
print iter.next()
print list(iter)

print map13.keys()
print map13.iterkeys()

print "------------------------------10----------------------------------------"
map15 = dict()
map15['a'] = "a11"
map15['b'] = "b11"
print map15
print map15.items()
for k, v in map15.items():
    print k
    print v














