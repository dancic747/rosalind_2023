#BA4e
'''Find a Cyclic Peptide with Theoretical Spectrum Matching an Ideal Spectrum'''

from amino_acid_mass import mass

def Expand(peptides):
    newPeptides=[]
    for peptide in peptides:
        for mass1 in masses:
            newPeptides.append(peptide+[mass1])
    return newPeptides
        
def Cyclospectrum(peptide):
    subpeptides=list()
    subpeptides.append(0)
    subpeptides.append(sum(peptide))

    dummy=peptide+peptide
    for i in range(1,len(peptide)):
        for j in range(0,len(peptide)):
            subpeptide=dummy[j:(j+i)]
            subpeptides.append(sum(subpeptide))
    
    return sorted(subpeptides)

def Consistent(peptide):
    theoreticalSpectrum=[0,sum(peptide)]
    for i in range(1,len(peptide)):
        for j in range(0,len(peptide)-i+1):
            subpeptide=peptide[j:(j+i)]
            theoreticalSpectrum.append(sum(subpeptide))

    
    for el in theoreticalSpectrum:
        if el in spectrum:
            flag=True
        else:
            flag=False
            break
    return flag

def CyclopeptideSequencing(spectrum):
    peptides=[[]]
    res=[]
    while len(peptides)>0:
        peptides=Expand(peptides)
        for peptide in peptides:
            if sum(peptide)==max(spectrum):
                if Cyclospectrum(peptide)==spectrum:
                    res.append(peptide)
                peptides.remove(peptide)
            elif Consistent(peptide)==False:
                peptides=[p for p in peptides if p!=peptide]
    return res

if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba4e.txt", "r") as f:
        spectrum=f.readline().strip().split(' ')

    for i in range(len(spectrum)):
        spectrum[i]=int(spectrum[i])
    
    masses=list(set(mass.values()))
    res=CyclopeptideSequencing(spectrum)
    
    for r in res:
        print('-'.join(map(str,r)),end=' ',file=open('output.txt','a'))