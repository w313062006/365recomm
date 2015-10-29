import csv
import random

PROJECT_ID = {}
def getProjectId():
    global PROJECT_ID
    with open('/home/wushuang/Downloads/365/relate-info/DWB_NEW_PROJECT.csv','r') as input:
        csvFile = csv.reader(input)
        for index,i in enumerate(csvFile):
            if index != 0:
                PROJECT_ID.update({i[1] + '-' + i[2]:index})
        input.close()
def findid(x):
    return str(PROJECT_ID[x])
def main():
    item_dic = {}
    lines = open('FCresult1902.txt','r').readlines()
    for i in lines:
        tmp = i.strip().split(' ')
        if len(tmp) > 1:
            for k in tmp:
                if item_dic.has_key(k) :
                    item_dic[k].update(filter(lambda x:x != k,tmp))
                else:
                    item_dic.update({k:set(filter(lambda x:x != k,tmp))})
    #print len(item_dic)


    item_dic = sorted(item_dic.items(),key=lambda x:int(x[0][x[0].rfind('-')+1:]))
    getProjectId()

    output =open('recomm_result.txt','w')

    for i in item_dic:

        tmp_len = len(list(i[1])[:10])
        if tmp_len < 10:
            a = ' 0' * (10-tmp_len)
            b1 = ' '.join(map(lambda x:findid(x),list(i[1])[:10]))
            output.write(findid(i[0]) + ' ' + b1 + a +'\n')
        else:
            b2 = ' '.join(map(lambda x:findid(x),random.sample(list(i[1]),10)))
            output.write(findid(i[0]) + ' ' + b2 +'\n')

if __name__ == '__main__':
    main()