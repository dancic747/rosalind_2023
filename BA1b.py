#BA1b
'''Find the Most Frequent Words in a String'''

def frequentWords(text,k):
    d=dict()
    for i in range(len(text)-k+1):
        if text[i:i+k] not in d: d[text[i:i+k]]=1
        else: d[text[i:i+k]]+=1
    
    m=max(d.values())
    res=list()
    for key in d.keys():
        if d[key]==m: res.append(key)
    
    return res


if __name__=="__main__":
    with open("C:/Users/Y530/Downloads/rosalind_ba1b.txt", "r") as f:
        text=f.readline().strip()
        k=int(f.readline().strip())
    
    r=frequentWords(text,k)
    print(*sorted(r), sep=' ')