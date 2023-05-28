#BA3e
'''Construct the De Bruijn Graph of a Collection of k-mers'''

def prefix(s):
    return s[0:len(s)-1]

def suffix(s):
    return s[1:]


def deBruin2(dnaList):
    d=dict()
    for dna in dnaList:
        if prefix(dna) not in d.keys(): d[prefix(dna)]=[suffix(dna)]
        else: d[prefix(dna)].append(suffix(dna))
    return d


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba3e.txt", "r") as f:
        dnaList=f.read().split()
    
    d=deBruin2(dnaList)
    for key in sorted(d.keys()):
        print(key + ' -> ' + ','.join(sorted(d[key])),file=open('output.txt','a'))