#BA3c
'''Construct the Overlap Graph of a Collection of k-mers'''

def prefix(s):
    return s[0:len(s)-1]

def suffix(s):
    return s[1:]

def overlapGraph(dnaList):
    d=dict()
    for dna in dnaList:
        d[dna]=list()
    
    for key in d.keys():
        for dna in dnaList:
            if dna!=key and suffix(key)==prefix(dna): d[key].append(dna)
    
    return d

if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba3c.txt", "r") as f:
        dnaList=f.read().split()
    
    d=overlapGraph(dnaList)
    for key in sorted(d.keys()):
        for value in sorted(d[key]):
            print(key+' -> '+value,file=open('output.txt','a'))