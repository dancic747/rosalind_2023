#BA4d
'''Compute the Number of Peptides of Given Total Mass'''

from amino_acid_mass import mass


def countPeptides(m,d,aaMasses):
    if m<0: return 0
    elif m==0: return 1
    elif m in d.keys(): return d[m]
    else:
        d[m]=0
        for aaMass in aaMasses:
            d[m]+=countPeptides(m-aaMass,d,aaMasses)
    return d[m]



if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba4d.txt", "r") as f:
        m=int(f.readline().strip())

    d=dict()
    aaMasses=set(mass.values())
    res=countPeptides(m,d,aaMasses)
    print(res)
    