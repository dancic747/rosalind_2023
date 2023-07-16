#BA5e
'''Find a Highest-Scoring Alignment of Two Strings'''

from blosum62 import BLOSUM62


def globalAlignment(str1, str2, indelPenalty):
    str1 = "-" + str1
    str2 = "-" + str2

    scoreMatrix=list()
    for i in range(len(str1)):
        scoreMatrix.append([0]*len(str2))

    backtrackMatrix=list()
    for i in range(len(str1)):
        backtrackMatrix.append(['']*len(str2))

    for j in range(len(str2)):
        scoreMatrix[0][j] = -indelPenalty * j
        backtrackMatrix[0][j] = "right"

    for i in range(len(str1)):
        scoreMatrix[i][0] = -indelPenalty * i
        backtrackMatrix[i][0] = "down"

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if (str1[i], str2[j]) in BLOSUM62:
                key = (str1[i], str2[j])
            else:
                key = (str2[j], str1[i])
            score1 = scoreMatrix[i - 1][j - 1] + BLOSUM62[key]
            score2 = scoreMatrix[i - 1][j] - indelPenalty
            score3 = scoreMatrix[i][j - 1] - indelPenalty
            scoreMatrix[i][j] = max(score1, score2, score3)
            if scoreMatrix[i][j] == score1:
                backtrackMatrix[i][j] = "diag"
            elif scoreMatrix[i][j] == score2:
                backtrackMatrix[i][j] = "down"
            elif scoreMatrix[i][j] == score3:
                backtrackMatrix[i][j] = "right"

    i = len(str1) - 1
    j = len(str2) - 1
    newString1 = ""
    newString2 = ""
    while i != 0 or j != 0:
        direction = backtrackMatrix[i][j]
        if direction == "diag":
            newString1 = str1[i] + newString1
            newString2 = str2[j] + newString2
            i -= 1
            j -= 1
        elif direction == "down":
            newString1 = str1[i] + newString1
            newString2 = "-" + newString2
            i -= 1
        else:
            newString1 = "-" + newString1
            newString2 = str2[j] + newString2
            j -= 1

    return scoreMatrix[len(str1) - 1][len(str2) - 1], newString1, newString2


if __name__=='__main__':
    with open("C:/Users/Y530/Downloads/rosalind_ba5e.txt", "r") as f:
        string1=f.readline().strip()
        string2=f.readline().strip()

    indelPenalty=5
    res,str1,str2=globalAlignment(string1,string2,5)
    print(res)
    print(str1)
    print(str2)