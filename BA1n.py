#BA1n
'''Generate the d-Neighborhood of a String'''

from itertools_dict import allKmersDict
from BA1g import hamming

def dNeighbourhood(pattern,d):
    dic=allKmersDict(len(pattern))
    neighbours=list()
    for key in dic.keys():
        if hamming(pattern,key)<=d: neighbours.append(key)
    return neighbours


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba1n.txt", "r") as f:
        pattern=f.readline().strip()
        d=int(f.readline().strip())
    
    res=dNeighbourhood(pattern,d)
    print(*res,sep='\n', file=open('output.txt','w'))