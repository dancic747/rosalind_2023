#BA1e
'''Find Patterns Forming Clumps in a String'''

def minTOccurances(genome,k,t):
    d=dict()
    for i in range(len(genome)-k+1):
        if genome[i:i+k] not in d: d[genome[i:i+k]]=1
        else: d[genome[i:i+k]]+=1
    
    res=list()
    for key in d.keys():
        if d[key]>=t: res.append(key)
    return res


def clumpFindingProblem(dna,k,L,t):
    #k - kmer
    #L - len of genome
    #t - min number of occurances of kmer in genome
    res=list()
    for i in range(len(dna)-L+1):
        res+=minTOccurances(dna[i:i+L],k,t)
    return res

if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba1e.txt", "r") as f:
        dna=f.readline().strip()
        int_params=f.readline().strip() #looks smth like "3 35 5" (i.e. it's string, not list)
    k,L,t=int_params.split(' ')
   
    
    res=set(clumpFindingProblem(dna,int(k),int(L),int(t)))
    print(*res, sep=' ', file=open('output.txt','w'))