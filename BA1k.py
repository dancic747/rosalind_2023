#BA1k
'''Generate the Frequency Array of a String'''

from itertools_dict import allKmersDict

def freqArray(dna,k):
    d=allKmersDict(k)
    for i in range(len(dna)-k+1):
        for key in d.keys():
            if key==dna[i:i+k]: d[key]+=1
    
    freq=list()
    for key in sorted(d.keys()):
        freq.append(d[key])
    return freq

if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba1k.txt", "r") as f:
        dna=f.readline().strip()
        k=int(f.readline().strip())
    res=freqArray(dna,k)
    print(*res, sep=' ', file=open('output.txt','w'))