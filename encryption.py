"""
Solution to hackerrank.com/challenges/encryption
"""

import math

s = input().strip()

l_s = len(s)
r_f = math.floor(math.sqrt(l_s))
r_c = math.ceil(math.sqrt(l_s))

if (r_f * r_f) >= l_s:
    row = col = r_f
elif (r_f * r_c) >= l_s:
    row, col = r_f, r_c
else:
    row = col = r_c

row_list = []
j = 0
for i in range(row):
    row_list.append(s[j:j+col])
    j += col
new_list = []
for i in range(col):
    try:
        new_list.append("".join([j[i] for j in row_list]))
    except:
        new_list.append("".join([j[i] for j in row_list[:-1]]))
print(" ".join([i for i in new_list]))
