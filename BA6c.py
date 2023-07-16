#BA6c
'''Compute the 2-Break Distance Between a Pair of Genomes'''


def blocks(p):
    elements=0
    for c in p:
        elements=elements+len(c)
    return elements


def ChromosomeToCycle(Chromosome):
    Nodes=[]
    for j in range(0,len(Chromosome)):
        i=Chromosome[j]
        if i > 0:
            Nodes.append(2*i-1)
            Nodes.append(2*i)
        else:
            Nodes.append(-2*i) #minus because i is negative
            Nodes.append(-2*i-1)
    return Nodes


def ColoredEdges(P):
    Edges = []
    for Chromosome in P:
        Nodes = ChromosomeToCycle(Chromosome)
        for j in range(len(Chromosome)):
            Edges.append((Nodes[2 * j + 1], Nodes[(2 * j + 2) % len(Nodes)]))
    return Edges


def cycles(p,q):
    e=ColoredEdges(p)
    e+=ColoredEdges(q)
    c=0
    nodes=[]
    for i in range (2*blocks(p)):
        nodes.append(i)
    while len(e)>0:
        first=e[0][0]
        second=e[0][1]
        e.remove(e[0])
        while second!=first:
            for edge in e:
                if edge[0]==second:
                    second=edge[1]
                    e.remove(edge)
                    break
                if edge[1]==second:
                    second = edge[0]
                    e.remove(edge)
                    break
        c=c+1
    return c



if __name__ == '__main__':

    with open('C:/Users/Y530/Downloads/rosalind_ba6c.txt','r') as f:
        P=f.readline().strip()
        Q=f.readline().strip()
    
    
    p = P.split(")(")
    p[0] = p[0][1:]
    p[len(p) - 1] = p[len(p) - 1][:-1]
    for j in range(len(p)):
        p[j] = p[j].split(" ")
        for i in range(len(p[j])):
            p[j][i] = int(p[j][i])
    q = Q.split(")(")
    q[0] = q[0][1:]
    q[len(q) - 1] = q[len(q) - 1][:-1]
    for j in range(len(q)):
        q[j] = q[j].split(" ")
        for i in range(len(q[j])):
            q[j][i] = int(q[j][i])
    
    res = blocks(p) - cycles(p, q)
    print(res)