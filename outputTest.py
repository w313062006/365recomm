import csv
recomm_dic = {}

def check_num(str):
    return int(str)

dic_file = open('recomm_result.txt','r')
lines = dic_file.readlines()

for i in lines:
    line_list = i.strip().split(' ')
    recomm_dic.update({int(line_list[0]):map(lambda x:int(x),line_list[1:])})
#print recomm_dic

step = []
with open('/home/wushuang/Downloads/365/relate-info/testUserVisitHouse99.csv','r') as input:
    csvFile = csv.reader(input)
    for row in csvFile:
        step.append(','.join(filter(lambda x:check_num(x) > 0,row[:-1])))
output =open('test_result5.txt','w')
for i in step:
    stepslist = i.split(',')
    if len(stepslist) > 1 :
        #print stepslist


        for index,j in enumerate(stepslist[1:]):
            if recomm_dic.has_key(int(stepslist[index])):
                output.write(j + ' ' + ' '.join(map(lambda x:str(x),recomm_dic[int(stepslist[index])])) + '\n')
