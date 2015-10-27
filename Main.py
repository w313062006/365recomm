import os
import csv

#log-file dir
G_LOG_FILE_DIR = '/home/wushuang/Downloads/365/3month-logs1'

#log-file list
G_LOG_FILE_LIST = []

#Project file dir
G_PROJECT_DIR = '/home/wushuang/Downloads/365/relate-info/DWB_NEW_PROJECT.csv'
G_PROJECT_LIST = frozenset()

#output data
G_OUTPUT = []
#
G_DIC = {}


def outputCleanedData(tmp_dir):
    global G_OUTPUT
    f = open(tmp_dir,'w')

    for i in G_OUTPUT:
        t = ','.join(i)
        f.write(t + '\n')

def checkProjectValue(line):
    if len(line) > 2 and line[-2] in G_PROJECT_LIST:
        return 1
    else:
        return 0

def getProjectInfo():
    global G_PROJECT_DIR,G_PROJECT_LIST
    with open(G_PROJECT_DIR) as input:
        csvFile = csv.reader(input)
        tmp_code = map(lambda x:x[1]+'-'+x[2],csvFile)
        G_PROJECT_LIST = frozenset(tmp_code)
def getLogData(f_Path):
    global G_LOG_FILE_LIST,G_OUTPUT

    G_LOG_FILE_LIST = filter(lambda x:os.path.isfile(x) == True,map(lambda x:f_Path + '/' + x,os.listdir(f_Path)))

    for a in G_LOG_FILE_LIST:
        try:
            file = open(a)
            getProjectInfo()
        except:
            print 'Open File('+ a +') error'
            raise
        while 1:
            tmp_line = file.readline()
            if tmp_line != '':
                tmp_content =map(lambda x:x[1:-1],tmp_line.strip().split(','))
                if checkProjectValue(tmp_content) == 1:
                    G_OUTPUT.append(tmp_content)
                    tmp_key = '-'.join(tmp_content[5:7])
                    tmp_value = tmp_content[-2]

                    if G_DIC.has_key(tmp_key):
                        G_DIC[tmp_key].update([tmp_value])
                    else:
                        G_DIC.update({tmp_key:set([tmp_value])})
                else:
                    continue
            else:
                break
        outputPath = a[:a.rfind('/')] + '/out/'
        if os.path.exists(outputPath):
            pass
        else:
            os.mkdir(outputPath)
        outputCleanedData(outputPath + a[a.rfind('/')+1:] + '-out')
        G_OUTPUT = []
        file.close()
def main():
    global G_PROJECT_DIR
    getLogData(G_LOG_FILE_DIR)
    pass
if __name__ == '__main__':
    main()