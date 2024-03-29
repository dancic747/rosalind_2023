#BA2g
'''Implement GibbsSampler'''

def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]

def Lwindows(text,L):
    """list of all L-windows in text"""
    windows=list()
    for i in range (0,len(text)-L+1):
        windows.append(kmer(text,i,L))
    return windows

def probability(window,profile):
    # probability of kmer in string according to profile matrix
    prob=1
    for i in range (0,len(window)):
        if window[i]=='A':
            prob=prob*float(profile[0][i])
        else:
            if window[i]=='C':
                prob = prob * float(profile[1][i])
            else:
                if window[i] == 'G':
                    prob = prob * float(profile[2][i])
                else:
                    if window[i] == 'T':
                        prob = prob * float(profile[3][i])

    return prob

def mostProbkmerinText(text,k,profile):
    d=dict()
    for window in Lwindows(text,k):
        d[window]=probability(window,profile)
    return  [x[0] for x in d.items() if x[1]==max(d.values())][0]

def count(motifs,nucl,i):
    # compute count for each nucleotide of i-th column
    col=[motif[i] for motif in motifs]
    num=0
    if nucl==0:
        num=len([n for n in col if n=='A'])
    if nucl==1:
        num=len([n for n in col if n=='C'])
    if nucl==2:
        num=len([n for n in col if n=='G'])
    if nucl==3:
        num=len([n for n in col if n=='T'])
    return num

def capitalLetter(motifs,i):
    # find a capital letter of i-th column
    counts=[count(motifs,nucl,i) for nucl in range (0,4)]
    return [nucl for nucl in range (0,4) if counts[nucl]==max(counts)][0]

def score(motifs):
    sc=0
    for i in range(0,len(motifs[0])):
        sc=sc+(len(motifs)-count(motifs,capitalLetter(motifs,i),i))
    return  sc

def profileMatrixWithPseudocounts(motifs,k):
    matrix=list()
    for i in range(0,k):
        for nucl in range(0,4):
            matrix.append(list())
            matrix[nucl].append((count(motifs,nucl,i)+1) / (len(motifs)+4))
    return  matrix

def Motifs(dna, profile):
    t = len(dna)
    k = len(profile[0])
    motifs = []
    for i in range(0, t):
        motifs.append(mostProbkmerinText(dna[i], k, profile))
    return motifs

def RandomizedMotifSearchAtom(dna, k):
    import random
    n = len(dna[0])
    randpos = [random.randint(0, n - k) for i in range(0, len(dna))]
    #zip(randpos, dna)=[(poz1,dna1),...,(pozt,dnat)]
    #bestmotifs=[dna1[poz1,poz1+k],...,dnat[pozt,pozt+k]]
    bestmotifs = [x[1][x[0] : (x[0] + k)] for x in zip(randpos, dna)]
    motifs = bestmotifs
    while True:
        profile = profileMatrixWithPseudocounts(motifs,k)
        motifs = Motifs(dna, profile)
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
        else:
            return bestmotifs

def ProfileRandomlyGeneratedKmer(text, profile, k):
    import random
    L = []
    for i in range(0, len(text) - k + 1):
        L.append(probability(text[i : i + k], profile))
    C = sum(L)
    L = [x / C for x in L]
    r = random.uniform(0, 1)
    s = 0
    for ind, x in enumerate(L):
        s = s + x
        if r < s:
            return text[ind : ind + k]

def GibbsSamplerAtom(dna, k, N=1000):
    import random
    t = len(dna)
    bestmotifs = RandomizedMotifSearchAtom(dna, k)
    motifs = list(bestmotifs)
    for j in range(1, N):
        i = random.randint(0, t - 1)
        #tmp=list(motifs) because tmp.pop() would pop the element from motifs
        tmp = list(motifs)
        tmp.pop(i)
        profile = profileMatrixWithPseudocounts(tmp,len(tmp[0]))
        motifs[i] = ProfileRandomlyGeneratedKmer(dna[i], profile, k)
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
    return bestmotifs

def GibbsSampler(dna, k, repeats=20, N=1000):
    bestmotifs = GibbsSamplerAtom(dna, k, N)
    for i in range(1, repeats):
        motifs = GibbsSamplerAtom(dna, k, N)
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
    return bestmotifs

if __name__ == '__main__':
    with open('C:/Users/Y530/Downloads/rosalind_ba2g.txt','r') as f:
        k,t,N=f.readline().strip().split(' ')
        dna=f.read().splitlines()

    k=int(k)
    t=int(t)
    N=int(N)

    res=GibbsSampler(dna, k, 20, 1000)
    print("\n".join(res),file=open('output.txt','w'))