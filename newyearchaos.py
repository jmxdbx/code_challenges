"""
Solution to hackerrank.com/challenges/new-year-chaos
"""
def merge_sort(q):
    if len(q) < 2:
        return 0, q
    mid = len(q)//2
    left_inversions, left = merge_sort(q[:mid])
    right_inversions, right = merge_sort(q[mid:])
    m_inversions, merged = merge(left, right)
    inversions = left_inversions + right_inversions + m_inversions
    return inversions, merged

def merge(left, right):
    res = []
    i = j = inversions = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            inversions += j
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    inversions += j * (len(left) - i)
    res += left[i:]
    res += right[j:]
    return inversions, res

def numbribes(q):
    for j in range(len(q)):
        if (q[j] - j - 1) > 2:
            return "Too chaotic"
    inversions, m = merge_sort(q)
    return inversions

for t in range(int(input().strip())):
    n = int(input().strip())
    q = [int(i) for i in input().strip().split()]
    print(numbribes(q))
