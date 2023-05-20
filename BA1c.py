#BA1c
'''Find the Reverse Complement of a String'''

def reverseComplement(dna):
    reverse=''
    for i in dna[::-1]:
        if i=='A': reverse+='T'
        elif i=='T': reverse+='A'
        elif i=='G': reverse+='C'
        elif i=='C': reverse+='G'
        else: "error"
    return reverse


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba1c.txt", "r") as f:
        dna=f.readline().strip()
    r=reverseComplement(dna)
    print(r)