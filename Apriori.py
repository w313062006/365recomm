from operator import and_
import csv


class Apriori():
    TYPE = 'YES'
    MIN_SUPPORT = 0.01
    K ={}
    def __init__(self,projectFile,transacFile):

        self.projectInfo = set([])
        self.transacInfo = []

        with open(projectFile) as Pfile:
            csvFile = csv.reader(Pfile)
            tmp_code = map(lambda x:x[1]+'-'+x[2],csvFile)
            for i in tmp_code:
                self.projectInfo.add(i)
        Pfile.close()

        with open(transacFile) as Tfile:
            self.transacInfo = map(lambda x:set(x[x.rfind(':')+1:].strip().split(',')),Tfile.readlines())
    def getSupport(self,transet):
        if type(transet) != frozenset:
            transet = frozenset([transet])
        #print items
        count = 0
        for i in self.transacInfo:
            if transet & i == transet:
                    count = count + 1
        return float(count)/float(len(self.transacInfo))
    def genItemsSupports(self,k_item):
        if k_item - 1:
            subSet = frozenset([i.union(j) for i in self.K.keys() for j in self.K.keys() if len(i.union(j)) == k_item])
            C_k = filter(lambda x:x.items()[0][1]>self.MIN_SUPPORT,map(lambda x:{x:self.getSupport(x)},subSet))
            if len(C_k) == 0:
                self.TYPE = 'Done'
            else:
                for i in C_k:
                    self.K.update(i)

            #1-itemsSet
        else:
            #a = map(lambda x:{frozenset([x]):self.getSupport(x)},self.projectInfo)

            for i in filter(lambda x:x.items()[0][1]>self.MIN_SUPPORT,map(lambda x:{frozenset([x]):self.getSupport(x)},self.projectInfo)):
                self.K.update(i)
            pass
    def runApriori(self):
        k = 1
        while k:
            self.genItemsSupports(k_item = k)
            if self.TYPE == 'YES':
                k = k + 1
            else:
                break

        #tmp_dic = sorted(self.K.iteritems(),key = lambda d:list(d[0]),reverse=False)

        f = open('result.txt','w')

        for i in self.K.items():
            t = ' '.join(list(i[0]))
            f.write(t + ' ' + '%.5f'%i[1] + '\n')

a = Apriori('/home/wushuang/Downloads/365/relate-info/DWB_NEW_PROJECT.csv','/home/wushuang/Downloads/365/3month-logs/out/Cresult.txt')

a.runApriori()
