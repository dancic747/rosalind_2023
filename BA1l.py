#BA1l
'''Implement PatternToNumber'''

def symbolToNumber(symbol):
    if symbol=='A': return 0
    elif symbol=='C': return 1
    elif symbol=='G': return 2
    elif symbol=='T': return 3

def patternToNumber(pattern):
    if pattern=='': return 0
    symbol=pattern[-1]
    prefix=pattern[:len(pattern)-1]
    return 4*patternToNumber(prefix)+symbolToNumber(symbol)


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba1l.txt", "r") as f:
        pattern=f.readline().strip()
    res=patternToNumber(pattern)
    print(res)