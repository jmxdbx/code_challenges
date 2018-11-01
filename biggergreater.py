"""
Solution to hackerrank.com/challenges/bigger-is-greater
"""

def lex(st):
    for i in range(len(st)-2, -1, -1):
        if st[i] < st[i+1]:
            prefix = st[:i]
            for j in range(len(st)-1, i, -1):
                if st[j] > st[i]:
                    break
            prefix += st[j]
            ind = j
            for k in range(len(st)-1, i, -1):
                if k == ind:
                    prefix += st[i]
                else:
                    prefix += st[k]
            return prefix
    return "no answer"

for i in range(int(input())):
    print(lex(input().strip()))
