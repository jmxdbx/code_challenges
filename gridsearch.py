"""
Solution to hackerrank.com/challenges/the-grid-search
Author: Joel Berry
"""

def grid(G, P):
    for i in range(len(G) - len(P) + 1):
        if P[0] in G[i]:
            for m in range(len(G[0]) - len(P[0]) + 1):
                if G[i][m:m + len(P[0])] == P[0]:
                    match = True
                    for k in range(len(P)-1):
                        if G[i+k+1][m:m + len(P[0])] != P[k+1]:
                            match = False
                    if match:
                        return True
    return False




t = int(input().strip())
for a0 in range(t):
    R,C = [int(i) for i in input().strip().split()]
    G = []
    for i in range(R):
        G.append(str(input().strip()))
    r,c = [int(i) for i in input().strip().split()]
    P = []
    for i in range(r):
        P.append(str(input().strip()))

    print("YES") if grid(G,P) else print("NO")
