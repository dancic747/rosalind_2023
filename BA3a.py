#BA3a
'''Generate the k-mer Composition of a String'''

def kmerComposition(k,dna):
    res=list()
    for i in range(len(dna)-k+1):
        res.append(dna[i:i+k])
    return sorted(res)


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba3a.txt", "r") as f:
        k=int(f.readline().strip())
        dna=f.read().strip()  
    
    res=kmerComposition(k,dna)
    print(*res, sep='\n',file=open('output.txt','w'))