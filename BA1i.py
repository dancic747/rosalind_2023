#BA1i
'''Find the Most Frequent Words with Mismatches in a String'''

from itertools_dict import allKmersDict
from BA1g import hamming

def mostMismatches(dna,k,mism):
    d=allKmersDict(k)
    for i in range(len(dna)-k+1):
        for key in d.keys():
            if hamming(key,dna[i:i+k])<=mism: d[key]+=1
    
    m=max(d.values())
    res=list()
    for key in d.keys():
        if d[key]==m: res.append(key)
    return res

if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba1i.txt", "r") as f:
        dna=f.readline().strip()
        k,mism=f.readline().split(' ')
    res=mostMismatches(dna,int(k),int(mism))
    print(*res, ' ', file=open('output.txt','w'))