# -*- coding:utf-8 -*-
__author__ = 'yangh'

data = [
    dict(C001="XiaoMing", C002="efg"),
    dict(C002="ZhongGuo", C005="456", C007="78999999999", C00="BBS", C100="NINI"),
    dict(C001="XiaoMing", C003="bbs"),
    dict(C006="ZhongGuo", C007="bbs"),
    dict(C007="ZhongGuo", C009="bbs")
]


cols_width=dict()

for d in data:
    for k,v in d.items():
        if k not in cols_width:
            cols_width[k] = len(k)+2
            pass
        v_len = len(v)+2
        if v_len > cols_width[k]:
            cols_width[k] = v_len
    pass

cols =cols_width.items()
cols.sort()
data_len = len(data)

index_w = max(len('index'), len(str(data_len))) +2

head_row = [('index', index_w)]+cols

print '+'.join(['-' * w for(c, w) in head_row])
print '|'.join([ k.center(w, ' ')  for (k, w) in head_row])
print '+'.join(['-' * w for(c, w) in head_row])

cols_width['index'] = index_w

for i in range(0,data_len):
    printMap = [];
    map = data[i]
    printMap.append( (str(i), index_w) )
    for k, v in cols:
        printMap.append( (map.get(k, ''), cols_width.get(k)) )
    print '|'.join([k.center(v, ' ')  for (k, v) in printMap])
    print '+'.join(['-' * w for(c, w) in head_row])
