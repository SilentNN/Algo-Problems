"""
Problem Statement #

Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""

def pair_with_targetsum(arr, target_sum):
    left = 0
    right = len(arr) - 1

    while (left < right):
        sum = arr[left] + arr[right];
        if sum == target_sum:
            return [left, right]
        if sum < target_sum:
            left += 1
        else:
            right -= 1
    return False

# print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
# print(pair_with_targetsum([2, 5, 9, 11], 11))

"""
Problem Statement #

Given an array of sorted numbers, remove all duplicates from it. 
You should not use any extra space; 
after removing the duplicates in-place return the new length of the array.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
"""

def remove_duplicates(arr):
    last = 1
    i = 1

    while i < len(arr):
        
    return


print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
remove_duplicates([2, 2, 2, 11])