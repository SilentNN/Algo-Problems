# Largest Difference

# Given an array of integers, find the largest difference between two elements 
# such that the element of lesser value must come before the greater element. Complete this problem in O(n) time.

from cmath import inf


def findLargestDifference(arr):
    maxDiff = -1
    minNum = arr[0]
    
    for i in range(1,len(arr)):
        minNum = min(minNum, arr[i])
        maxDiff = max(maxDiff, arr[i] - minNum)

    return maxDiff

# print(findLargestDifference([1, 6, 5, 2, 9, -2]))
# print(findLargestDifference([12,13,0,9]))

# Part 1: Say that I gave you an array of length n, 
# containing the numbers 1..n in jumbled order. "Sort" 
# this array in O(n) time. You should be able to do this without looking at the input.

def sort1(arr):
    sorted = []
    for i in range(len(arr)):
        sorted.append(i + 1)
    return sorted

# print(sort1([1, 6, 5, 2, 3, 4]))

# Part 2: Say that I give you an array of length n with numbers in the range 1..N (N >= n). 
# Sort this array in O(n + N) time. You may use O(N) memory.

def sort2(arr):
    seenNums = set()
    maxNum = -inf
    res = []

    for num in arr:
        seenNums.add(num)
        maxNum = max(num, maxNum)

    for i in range(1, maxNum+1):
        if i in seenNums:
            res.append(i)

    return res

print(sort2([12,13,1,9]))

# Part 3: Say I give you an array of n strings, each of length k. 
# I claim that, using merge sort, you can sort this in O(knlog(n)), 
# since comparing a pair of strings takes O(k) time.

# I want you to beat that. Sort the strings in O(kn). 
# Hint: do not compare any two strings. You may assume all strings 
# contain only lowercase letters a..z without whitespace or punctuation.

def sort3(arr):
    return

print(sort3(['cat', 'car', 'bat', 'cry']))

"""
['cat', 'car', 'bat', 'cry']
[['bat'], ['cat', 'car', 'cry']]
[[['bat']], [[['car', 'cat'], ['cry']]]]
['bat', 'car', 'cat', 'cry']
"""