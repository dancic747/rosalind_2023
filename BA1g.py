#BA1g
'''Compute the Hamming Distance Between Two Strings'''

def hamming(s1,s2):
    c=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]: c+=1
    return c

if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba1g.txt", "r") as f:
        s1=f.readline().strip()
        s2=f.readline().strip()
    res=hamming(s1,s2)
    print(res)