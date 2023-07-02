#BA3f
'''Find an Eulerian Cycle in a Graph'''

import random


def findCycle(d):
  cycle=list()
  newStart=random.choice(list(d.keys()))
  cycle.append(newStart)

  while(d!={}):
    if newStart in d.keys():
      if len(d[newStart])==1:
        x=d[newStart][0]
        cycle.append(x)
        d.pop(newStart)
        newStart=x
      else:
        x=random.choice(d[newStart])
        cycle.append(x)
        d[newStart].remove(x)
        newStart=x

    if len(cycle)>1 and cycle[0]==cycle[-1]:
      break
  
  return d, cycle


def eulerianCycle(lista):
  d=dict()
  for l in lista:
    if l.split(' -> ')[0] not in d.keys():
      d[l.split(' -> ')[0]]=list(l.split(' -> ')[1].split(','))
    else:
      d[l.split(' -> ')[0]]+=l.split(' -> ')[1].split(',')
  allCycles=list()

  while(d!={}):
    d,cyc=findCycle(d)
    allCycles.append(cyc)

  if len(allCycles)==1: # we found the longest EC in graph on the first try 
    return allCycles[0]
  else:
    res=allCycles[0] #we'll merge all shorter cycles into one, longer, cycle - we're starting with the first cycle we found and then we'll insert the remaining cycles into it
    allCycles.remove(res)
    while len(allCycles)!=0:
      for c in allCycles:
        for node in c:
          if node in res:
           # print('ubacujem '+edge+' iz '+' -> '.join(c))
            index_of_node_in_res=res.index(node)
            index_of_node_in_c=c.index(node)
            if index_of_node_in_c!=0: #how we insert the shorter graph depends on the index of node in c (index == 0 or index != 0)
              res=res[:index_of_node_in_res]+c[index_of_node_in_c:]+c[1:index_of_node_in_c]+res[index_of_node_in_res:]
            else:
              res=res[:index_of_node_in_res]+c+res[index_of_node_in_res+1:]
            allCycles.remove(c)
            break
        
    return res



if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba3f.txt", "r") as f:
        lista=f.read().splitlines()
    
    res=eulerianCycle(lista)
    print(*res,sep='->',file=open('output.txt','w'))