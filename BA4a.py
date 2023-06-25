#BA4a
'''Translate an RNA String into an Amino Acid String'''

from genetic_code_dict import genetic_code

def proteinTranslation(rna):
    res=''
    for i in range(0,len(rna)-3+1,3):
        if genetic_code[rna[i:i+3]]!='*': res+=genetic_code[rna[i:i+3]]
        else: break
    return res

if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba4a.txt", "r") as f:
        rna=f.readline().strip()
    
    res=proteinTranslation(rna)
    print(res,file=open('output.txt','w'))