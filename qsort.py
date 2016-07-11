"""
Solution to hackerrank.com/challenges/quicksort3
Author: Joel Berry
"""

def partition(arr, p, r):
    pivot = arr[r]
    i = p
    for j in range(p, r):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    print(" ".join([str(x) for x in arr]))
    return i

def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q-1)
        quicksort(arr, q+1, r)
    return arr

n = input().strip().split()
arr = [int(x) for x in input().strip().split()]
quicksort(arr, 0, len(arr)-1)
