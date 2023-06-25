#BA4b
'''Find Substrings of a Genome Encoding a Given Amino Acid String'''

from genetic_code_dict import genetic_code
from BA4a import proteinTranslation

def reverseComplement(rna):
    reverse=''
    for i in rna[::-1]:
        if i=='A': reverse+='U'
        elif i=='U': reverse+='A'
        elif i=='G': reverse+='C'
        elif i=='C': reverse+='G'
        else: "error"
    return reverse

def peptideEncoding(rna,peptide):
    res=list()
    for i in range(len(rna)-len(peptide)*3+1):
        if proteinTranslation(rna[i:i+len(peptide)*3])==peptide: res.append(rna[i:i+len(peptide)*3].replace('U','T'))

    rnaReverse=reverseComplement(rna)
    for i in range(len(rnaReverse)-len(peptide)*3+1):
        if proteinTranslation(rnaReverse[i:i+len(peptide)*3])==peptide:
            res.append(reverseComplement(rnaReverse[i:i+len(peptide)*3]).replace('U','T'))
    
    return res

if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba4b.txt", "r") as f:
        dna=f.readline().strip()
        peptide=f.readline().strip()
    
    rna=dna.replace('T','U')
    res=peptideEncoding(rna,peptide)
    print(*res,sep='\n',file=open('output.txt','w'))