#BA1a
'''Compute the Number of Times a Pattern Appears in a Text'''

def patternCount(text,pattern):
    c=0
    for i in range(len(text)-len(pattern)+1):
        if (text[i:i+len(pattern)]==pattern): c+=1
    return c


if __name__=="__main__":
    with open("C:/Users/Y530/Downloads/rosalind_ba1a.txt", "r") as f:
        text=f.readline().strip()
        pattern=f.readline().strip()
    c=patternCount(text,pattern)
    print(c)