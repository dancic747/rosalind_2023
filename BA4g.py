#BA4g
'''Implement LeaderboardCyclopeptideSequencing'''

from amino_acid_mass import mass


def expand(leaderboard):
    res=list()
    for el in leaderboard:
        for mass1 in masses:
            res.append(el+[mass1])
    return res


def cyclospectrum(peptide):
    subpeptides=list()
    subpeptides.append(0)
    subpeptides.append(sum(peptide))

    dummy=peptide+peptide
    for i in range(1,len(peptide)):
        for j in range(0,len(peptide)):
            subpeptide=dummy[j:(j+i)]
            subpeptides.append(sum(subpeptide))
    
    return sorted(subpeptides)


def score(peptide,spectrum):
    cycloSpectrum=cyclospectrum(peptide)

    allElements=set(cycloSpectrum+spectrum)
    c=0
    for el in allElements:
        c+=min(spectrum.count(el),cycloSpectrum.count(el))
    return c


def cut(leaderboard,spectrum,N):
    if len(leaderboard)<=N:
        return leaderboard
    
    d=dict()
    for i,peptide in enumerate(leaderboard):
        d[i]=score(peptide,spectrum)

    sort=sorted(d.values(),reverse=True)
    res=list()
    for key,value in d.items():
        if value>=sort[N-1]: res.append(leaderboard[key])

    return res


def LeaderboardCyclopeptideSequencing(spectrum,N):
    leaderboard=[[]]
    leaderPeptide=[]

    while len(leaderboard)>0:
        leaderboard=expand(leaderboard)
        for peptide in leaderboard:
            if sum(peptide)==spectrum[-1]:
                if score(peptide,spectrum)> score(leaderPeptide,spectrum):
                    leaderPeptide=peptide
            elif sum(peptide)>max(spectrum):
                leaderboard=[p for p in leaderboard if p!=peptide]
        leaderboard=cut(leaderboard,spectrum,N)
    return leaderPeptide



if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba4g.txt", "r") as f:
        N=int(f.readline().strip())
        spectrum=f.readline().strip().split(' ')

    for i in range(len(spectrum)):
        spectrum[i]=int(spectrum[i])
    
    masses=list(set(mass.values()))

    leaderPeptide=LeaderboardCyclopeptideSequencing(spectrum,N)
    for el in leaderPeptide:
        el=str(el)
    print(*leaderPeptide,sep='-',file=open('output.txt','w'))