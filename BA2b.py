#BA2b
'''Find a Median String'''

from itertools_dict import allKmersDict
from BA1g import hamming


def medianString(k,dnaList):
    d=allKmersDict(k)
    for key in list(d.keys()):
        for i in range(len(dnaList)):
            hammingDistances=list()
            for j in range(len(dnaList[i])-k+1):
                hammingDistances.append(hamming(dnaList[i][j:j+k],key))
            d[key]+=min(hammingDistances)
    
    res=list()
    for key in d.keys():
        if d[key]==min(d.values()): res.append(key)
    return res


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba2b.txt", "r") as f:
        k=int(f.readline())
        dnaList=f.read().split()  

    res=medianString(k,dnaList)
    print(res[0], sep=' ')