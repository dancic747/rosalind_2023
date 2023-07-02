#BA3g
'''Find an Eulerian Path in a Graph'''

from BA3f import *


def eulerianPath(lista):
  d=dict()
  for l in lista:
    if l.split(' -> ')[0] not in d.keys():
      d[l.split(' -> ')[0]]=list(l.split(' -> ')[1].split(','))
    else:
      d[l.split(' -> ')[0]]+=l.split(' -> ')[1].split(',')
  dvalue=list()
  for key in d.keys():
    dvalue+=d[key]

  for i in list(set(dvalue)):
    if i not in list(d.keys()): newOut=i

  for key in d.keys():
    if len(d[key])!=dvalue.count(key): newIn=key

  lista.append(str(newOut)+' -> '+str(newIn))

  cycle=eulerianCycle(lista)
  res=cycle[cycle.index(newOut)+1:-1]+cycle[:cycle.index(newOut)+1]

  return res



if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba3g.txt", "r") as f:
        lista=f.read().splitlines()
    
    res=eulerianPath(lista)
    print(*res,sep='->',file=open('output.txt','w'))