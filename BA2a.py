#BA2a
'''Implement MotifEnumeration'''

from itertools_dict import allKmersDict
from BA1g import hamming

def motifEnumeration(k,d,dnaList):
    keyList=list(allKmersDict(k).keys())
    patterns=list()
    c=0
    for key in keyList:
        c=0
        for i in range(len(dnaList)):
            for j in range (len(dnaList[i])-k+1):
                if hamming(dnaList[i][j:j+k],key)<=d:
                    c+=1
                    break
        if c==len(dnaList) and key not in patterns: patterns.append(key)
            
    return patterns


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba2a.txt", "r") as f:
        k,d=f.readline().split()
        dnaList=f.read().split()
    
    res=motifEnumeration(int(k),int(d),dnaList)
    print(*sorted(res), sep=' ', file=open('output.txt','w'))