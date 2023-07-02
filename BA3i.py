#BA3i
'''Find a k-Universal Circular String'''

import itertools
from BA3f import *


def make_list(k):
  kmers=list(itertools.product(['0','1'], repeat=k))
  for i in range(len(kmers)):
    kmers[i]=''.join(kmers[i])
  return kmers


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba3i.txt", "r") as f:
        k=int(f.readline().strip())
    
    lista=make_list(k) 
    newLista=list()
    for l in lista: #turning the elements of the list lista into desired input for eulerianCycle function (input = graph)
        newLista.append(l[:k-1]+' -> '+ l[1:])

    res=eulerianCycle(newLista)
    r=res[0]
    for i in range(1,len(res)-k+1): #since we're looking for circular string, we don't need the last (k-1) characters (the first and the last (k-1) characters are identical)
        r+=res[i][-1]
    print(r,file=open('output.txt','w'))