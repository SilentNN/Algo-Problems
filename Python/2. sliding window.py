# Problem Statement #

# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

# Example 1:

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# Example 2:

# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

def MaxSumSubArrayOfSizeK(a, k):
    high = sum(a[:k])
    current = high

    for i in range(len(a) - k):
        current = current - a[i] + a[i+k]
        high = max(current, high)

    return high

# print(MaxSumSubArrayOfSizeK([2, 1, 5, 1, 3, 2], 3)) #9
# print(MaxSumSubArrayOfSizeK([2, 3, 4, 1, 5], 2)) #7



# Problem Statement #

# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum 
# is greater than or equal to ‘S’. Return 0, if no such subarray exists.

# Example 1:

# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

# Example 2:

# Input: [2, 1, 5, 2, 8], S=7 
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

# Example 3:

# Input: [3, 4, 1, 1, 6], S=8 
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

def smallest_subarray_with_given_sum(s, arr):
    min_length = len(arr) + 1
    i=0
    length=1
    sum = arr[i]

    while i+length <= len(arr) and length != 0:
        if sum >= s:
            min_length = min(length, min_length)
            sum = sum - arr[i]
            i += 1
            length -= 1
        else:
            if i+length >= len(arr):
                break
            sum = sum + arr[i+length]
            length += 1

    if min_length > len(arr):
        return 0

    return min_length

# print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])) #2
# print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])) #1
# print(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])) #3




# Problem Statement #

# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Example 1:

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

# Example 2:

# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".

# Example 3:

# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

def longest_substring_with_k_distinct(str, k):
    max_length = 1
    start = 0
    chars = {}

    for end in range(len(str)):
        if str[end] not in chars:
            chars[str[end]] = 0
        chars[str[end]] += 1

        while len(chars) > k:
            chars[str[start]] -= 1
            if chars[str[start]] == 0:
                chars.pop(str[start])
            start += 1

        max_length = max(end - start + 1, max_length)

    return max_length

# print(longest_substring_with_k_distinct("araaci", 2))
# print(longest_substring_with_k_distinct("araaci", 1))
# print(longest_substring_with_k_distinct("cbbebi", 3))



# Problem Statement #

# Given an array of characters where each character represents a fruit tree, 
# you are given two baskets and your goal is to put maximum number of fruits in each basket. 
# The only restriction is that each basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree. 
# You will pick one fruit from each tree until you cannot, i.e., you will stop 
# when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.

# Example 1:

# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

# Example 2:

# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

def fruits_into_baskets(fruits):
    start = 0
    counts = {}
    max_fruits = 0

    for end in range(len(fruits)):
        if fruits[end] not in counts:
            counts[fruits[end]] = 0
        counts[fruits[end]] += 1

        while len(counts) > 2:
            counts[fruits[start]] -= 1
            if counts[fruits[start]] == 0:
                del counts[fruits[start]]
            start += 1
        
        max_fruits = max(end - start + 1, max_fruits)

    return max_fruits

# print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))
# print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))





# Problem Statement #

# Given a string, find the length of the longest substring which has no repeating characters.

# Example 1:

# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".

# Example 2:

# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".

# Example 3:

# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".

def non_repeating_substring(str):
    start = 0
    chars_index_map = {}
    max_length = 0

    for end in range(len(str)):
        if str[end] in chars_index_map:
            start = chars_index_map[str[end]] + 1
        chars_index_map[str[end]] = end

        max_length = max(end - start + 1, max_length)

    return max_length


# print(non_repeating_substring('aabccbb'))
# print(non_repeating_substring('abbbb'))
# print(non_repeating_substring('abccde'))



# Problem Statement #

# Given a string with lowercase letters only, 
# if you are allowed to replace no more than ‘k’ letters with any letter, 
# find the length of the longest substring having the same letters after replacement.

# Example 1:

# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

# Example 2:

# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

# Example 3:

# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

def length_of_longest_substring(str, k):
    start = 0
    max_repeating_letters = 0
    max_length = 0
    chars = {}

    for end in range(len(str)):
        if str[end] not in chars:
            chars[str[end]] = 0
        chars[str[end]] += 1
        max_repeating_letters = max(chars[str[end]], max_repeating_letters)

        while end-start+1 > max_repeating_letters + k:
            chars[str[start]] -= 1
            start += 1

        max_length = max(end-start+1, max_length)
            
    return max_length

# print(length_of_longest_substring('aabccbb', 2))
# print(length_of_longest_substring('abbcb', 1))
# print(length_of_longest_substring('abccde', 1))






# Problem Statement #

# Given an array containing 0s and 1s, if you are allowed to 
# replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

# Example 1:

# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

# Example 2:

# Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
# Output: 9
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.


def longest_subarray_with_ones_after_replacement(arr, k):
    start, zero_count, max_length = 0, 0, 0

    for end in range(len(arr)):
        if arr[end] == 0:5
            zero_count += 1

        
    return

print(longest_subarray_with_ones_after_replacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(longest_subarray_with_ones_after_replacement([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))