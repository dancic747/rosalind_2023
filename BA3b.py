#BA3b
'''Reconstruct a String from its Genome Path'''

def reconstruct(dnaList):
    res=dnaList[0]
    for i in range(1,len(dnaList)):
        res+=dnaList[i][-1]
    return res


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba3b.txt", "r") as f:
        dnaList=f.read().split()

    res=reconstruct(dnaList)
    print(res,file=open('output.txt','w'))