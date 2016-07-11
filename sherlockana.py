"""
Solution to hackerrank.com/challenges/sherlock-and-anagrams
Author: Joel Berry
"""

n = int(input())
for i in range(n):
    st = input().strip()
    length = len(st)
    count = 0
    lsts = []
    for i in range(length):
        sub = []
        for j in range(length):
            if j+i < length:
                sub.append(''.join(sorted(st[j:j+i+1])))
        lsts.append(sub)

    for lst in lsts:
        for i in range(len(lst) - 1):
            count += lst[i+1:].count(lst[i])
    print(count)
