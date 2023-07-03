#BA6a
'''Implement GreedySorting to Sort a Permutation by Reversals'''

def greedySorting(p):
    approxReversalDistance=0
    res=list()
    for k in range(len(p)):
        value=k+1
        if p[k]!='+'+str(value):
            p=kSorting(p,k)
            res.append(p.copy()) #python magic - copy() is needed since it stops the first element of res from being overwritten (smth with scope and references, etm)
            approxReversalDistance+=1
            if p[k]=='-'+str(value):
                p=kSorting(p,k)
                res.append(p.copy())
                approxReversalDistance+=1
    return res

def kSorting(p,k):
    value=k+1
    if ('+'+str(value)) in p: indexOfValue=p.index('+'+str(value))
    elif('-'+str(value)) in p: indexOfValue=p.index('-'+str(value))
    
    if p[k]=='-'+str(value): 
        p[k]=p[k].replace('-','+')
    else:
        substr=p[k:indexOfValue+1]
        for i in range(len(substr)):
            if substr[i][0]=='+': substr[i]=substr[i].replace('+','-')
            elif substr[i][0]=='-': substr[i]=substr[i].replace('-','+')
        substr=substr[::-1]
        p=p[:k]+substr+p[indexOfValue+1:]
    return p


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba6.txt", "r") as f:
        p=f.readline().strip().replace('(','').replace(')','').split(' ')

    res=greedySorting(p)
    for r in res:
        print('(',end='',file=open('output.txt','a'))
        print(*r,sep=' ',end='',file=open('output.txt','a'))
        print(')',file=open('output.txt','a'))