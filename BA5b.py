#BA5b
'''Find the Length of a Longest Path in a Manhattan-like Grid'''

def manhattanTourist(n,m,down,right):
    s=list()
    for i in range(n+1): 
        s.append((m+1)*[0])
    
    for i in range(1,n+1):
        s[i][0]=s[i-1][0]+int(down[i-1][0])

    for j in range(1,m+1):
        s[0][j]=s[0][j-1]+int(right[0][j-1])
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i][j]=max(s[i-1][j]+int(down[i-1][j]), s[i][j-1]+int(right[i][j-1]))
    
    return s[n][m]


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba5b.txt", "r") as f:
        input=f.read().splitlines()
    
    down=list()
    right=list()
    n,m=input[0].split()
    for i in range(1,int(n)+1):
        down.append(input[i].split())
    for j in range(int(n)+1):
        right.append(input[int(n)+2+j].split())
    
    res=manhattanTourist(int(n),int(m),down,right)
    print(res)