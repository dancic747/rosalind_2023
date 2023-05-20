#BA1m
'''Implement NumberToPattern'''

def numberToSymbol(index):
    if index==0: return 'A'
    elif index==1: return 'C'
    elif index==2: return 'G'
    elif index==3: return 'T'

def numberToPattern(index,k):
    if k==1: return numberToSymbol(index)
    prefixIndex=index//4
    r=index%4
    symbol=numberToSymbol(r)
    prefixPattern=numberToPattern(prefixIndex,k-1)
    return prefixPattern+symbol

if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba1m.txt", "r") as f:
        index=int(f.readline().strip())
        k=int(f.readline().strip())
    res=numberToPattern(index,k)
    print(res, file=open('output.txt','w'))