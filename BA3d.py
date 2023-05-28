#BA3d
'''Construct the De Bruijn Graph of a String'''

def prefix(s):
    return s[0:len(s)-1]

def suffix(s):
    return s[1:]

def deBrujin(k,dna):
    d=dict()
    for i in range(len(dna)-k+1):
        p=prefix(dna[i:i+k])
        if p in d.keys(): d[p].append(suffix(dna[i:i+k]))
        else: d[p]=[(suffix(dna[i:i+k]))]
    return d


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba3d.txt", "r") as f:
        k=int(f.readline().strip())
        dna=f.readline().strip()

    d=deBrujin(k,dna)
    for key in sorted(d.keys()):
        print(key + ' -> ' +  ','.join(sorted(d[key])),file=open('output.txt','a'))