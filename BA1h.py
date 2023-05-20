#BA1h
'''Find All Approximate Occurrences of a Pattern in a String'''

import BA1g as g

def approxOccurrences(pattern,dna,mism):
    positions=list()
    for i in range(len(dna)-len(pattern)+1):
        if g.hamming(pattern,dna[i:i+len(pattern)])<=mism: positions.append(i)
    return positions


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba1h.txt", "r") as f:
        pattern=f.readline().strip()
        dna=f.readline().strip()
        mism=int(f.readline().strip())
    
    res=approxOccurrences(pattern,dna,mism)
    print(*res,sep=' ', file=open('output.txt','w'))