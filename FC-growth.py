
"""
fc-tree format:
root 6
 son1 7
  grandson9
 son2 8
"""

class treeNode:
    def __init__(self,nameValue,numOccur,parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode
        self.children = {}

    def inc(self,numOccur):
        self.count += numOccur
    def disp(self,ind = 1):
        print ' '*ind,self.name,' ',self.count
        for child in self.children.values():
            child.disp(ind + 1)

def createTree(dataSet, minSup=1):
    headerTable = {}
    #go over dataSet twice
    #one time
    for trans in dataSet:
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    #remove 0 item
    for k in headerTable.keys():
        if headerTable[k] < minSup:
            del(headerTable[k])
    freqItemSet = set(headerTable.keys())
    if len(freqItemSet) == 0:
        #if no items meet minSup
        return None, None
    for k in headerTable:
        headerTable[k] = [headerTable[k], None]
    retTree = treeNode('Null Set', 1, None)
    #two time
    for tranSet, count in dataSet.items():
        localD = {}
        for item in tranSet:
            if item in freqItemSet:
                localD[item] = headerTable[item][0]
        if len(localD) > 0:
            #order by frequent num
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateTree(orderedItems, retTree, headerTable, count)
    return retTree, headerTable

def updateTree(items, inTree, headerTable, count):
    #if in retTree.children
    if items[0] in inTree.children:
        inTree.children[items[0]].inc(count)
    else:
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        if headerTable[items[0]][1] == None:

            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)

def updateHeader(nodeToTest, targetNode):
    #find the 2-last node
    while (nodeToTest.nodeLink != None):
        nodeToTest = nodeToTest.nodeLink

    nodeToTest.nodeLink = targetNode
def createInitSet(dataset):
    retDic = {}
    for trans in dataset:
        retDic[frozenset(trans)] = retDic.get(frozenset(trans),0) + 1
    return retDic

def getprefixPath(leafNode,prefixPath):
    if leafNode.parent != None:
       prefixPath.append(leafNode.name)

       getprefixPath(leafNode.parent,prefixPath)

def findPrefixPath(treeNode):
    condPats = {}
    while treeNode != None:
        prefixPath = []
        getprefixPath(treeNode, prefixPath)
        if len(prefixPath) > 1:

            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats


def mineTree(Tree,headerTable,minSup,prefixPath,frequentItem):
    items = [i[0] for i in sorted(headerTable.items(),key=lambda x:x[1])]
    for item in items:
        newfrequen = prefixPath.copy()
        newfrequen.add(item)
        frequentItem.append(newfrequen)
        print newfrequen,headerTable[item][0]
        Citems = findPrefixPath(headerTable[item][1])


        Ctree,Chead = createTree(Citems,minSup)
        if Chead != None:
            #print 'con tree is: ',newfrequen
            #Ctree.disp(1)
            mineTree(Ctree,Chead,minSup,newfrequen,frequentItem)


def main():
    G_LOG_FILE_DIR = '/home/wushuang/Downloads/365/3month-logs'
    m = open(G_LOG_FILE_DIR + '/out/' + 'Cresult.txt','r').readlines()
    t =[]
    for i in m:
        t.append(i[i.rfind(':')+1:].strip().split(','))
    initSet = createInitSet(t)
    myFPtree,myHeaderTab = createTree(initSet,395)
    frequeItems = []
    mineTree(myFPtree,myHeaderTab,395,set([]),frequeItems)
    m = open('FCresult15043.txt','w')
    for i in frequeItems:
        m.write(' '.join(list(i))+'\n')
    m.close()


if __name__ == '__main__':
    main()


