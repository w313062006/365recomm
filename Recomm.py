

def main():
    item_dic = {}
    lines = open('FCresult15043.txt','r').readlines()
    for i in lines:
        tmp = i.strip().split(' ')
        if len(tmp) > 1:
            for k in tmp:
                if item_dic.has_key(k) :
                    item_dic[k].update(filter(lambda x:x != k,tmp))
                else:
                    item_dic.update({k:set(filter(lambda x:x != k,tmp))})
    print len(item_dic)


    item_dic = sorted(item_dic.items(),key=lambda x:int(x[0][x[0].rfind('-')+1:]))

    for i in item_dic:
        a = ' 0' * (10-(len(list(i[1])[:10])))
        print i[0] + ' ' + ' '.join(list(i[1])[:10]) + a

if __name__ == '__main__':
    main()