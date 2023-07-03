#BA6b
'''Compute the Number of Breakpoints in a Permutation'''

def breakpoints(p):
    c=0
    for i in range(1,len(p)):
        if i==1 and p[i-1]!='+1': c+=1
        if (int(p[i])-int(p[i-1]))!=1: c+=1
    if p[-1]!='+'+str(len(p)): c+=1
    return c

if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba6b.txt", "r") as f:
        p=f.readline().strip().replace('(','').replace(')','').split(' ')
    res=breakpoints(p)
    print(res)
