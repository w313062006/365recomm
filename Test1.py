# -*- coding:utf-8 -*-

G_LOG_FILE_DIR = '/home/wushuang/Downloads/365/3month-logs'
m = open(G_LOG_FILE_DIR + '/out/' + 'Cresult.txt','r')
b = map(lambda x:x.strip(),m.readlines())
for i in b:
    index = i.rfind(':')
    i1 = i[:index]
    i2 = i[index+1:].split(',')
    i = i1 + ':' + ','.join(sorted(i2,key=(lambda x:int(x[x.rfind('-')+1:])),reverse = False))
    print i