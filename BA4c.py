#BA4c
'''Generate the Theoretical Spectrum of a Cyclic Peptide'''

from amino_acid_mass import mass

def theoreticalSpectrum(peptide):
    d={'':0}
    allElements=list()
    allElements.append('')
    
    for i in range(len(peptide)):
        dummyPeptide=peptide+peptide[:i]
        for j in range(len(dummyPeptide)-i):
            if dummyPeptide[j:j+i]!='': 
                if len(dummyPeptide[j:j+i])!=1: d[dummyPeptide[j:j+i]]=0
                else: d[dummyPeptide[j:j+i]]=mass[dummyPeptide[j:j+i]]
                allElements.append(dummyPeptide[j:j+i])
    
    d[peptide]=0
    allElements.append(peptide)

    for key in d.keys():
        if len(key)>1:
            for i in range(len(key)):
                d[key]+=mass[key[i]]
    
    res=list()
    for element in allElements:
        res.append(d[element])
    
    return sorted(res)


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba4c.txt", "r") as f:
        peptide=f.readline().strip()
    
    res=theoreticalSpectrum(peptide)
    print(*res,sep=' ',file=open('output.txt','w'))