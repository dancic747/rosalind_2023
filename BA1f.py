#BA1f
'''Find a Position in a Genome Minimizing the Skew'''

def minSkew(dna):
    s=0
    skews=list()
    skews.append(0)

    for i in dna:
        if i=='C':
            s-=1
            skews.append(s)
        elif i=='G':
            s+=1
            skews.append(s)
        else: skews.append(s)
    
    m=min(skews)
    positions=list()
    for i in range(len(skews)):
        if skews[i]==m: positions.append(i)
    return positions


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba1f.txt", "r") as f:
       dna=f.readline().strip()
    res=minSkew(dna)
    print(*res,sep=' ', file=open('output.txt','w'))
