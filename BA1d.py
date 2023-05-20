#BA1d
'''Find All Occurrences of a Pattern in a String'''

def patternMatching(pattern,text):
    res=list()
    for i in range(len(text)-len(pattern)+1):
        if pattern==text[i:i+len(pattern)]: res.append(i)
    return res

if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba1d.txt", "r") as f:
        pattern=f.readline().strip()
        text=f.readline().strip()
    res=patternMatching(pattern,text)
    print(*res, sep=' ', file=open('output.txt','w'))