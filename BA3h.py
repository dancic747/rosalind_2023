#BA3h
'''Reconstruct a String from its k-mer Composition'''

from BA3g import *


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba3h.txt", "r") as f:
        k=int(f.readline().strip())
        lista=f.read().splitlines()

    newLista=list()

    for l in lista:
        newLista.append(l[:k-1]+' -> '+ l[1:])

    path=eulerianPath(newLista) #turning the elements of the list lista into desired input for eulerianPath function (input = graph)
    res=path[0]
    for i in range(1,len(path)):
        res+=path[i][-1]
    print(res,file=open('output.txt','w'))