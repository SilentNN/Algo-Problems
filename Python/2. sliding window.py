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
        if arr[end] == 0:
            zero_count += 1
        if zero_count > k:
            if arr[start] == 0:
                zero_count -= 1
            start += 1
        max_length = max(end - start + 1, max_length)
    return max_length

# print(longest_subarray_with_ones_after_replacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
# print(longest_subarray_with_ones_after_replacement([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))



# Permutation in a String (hard) #

# Given a string and a pattern, find out if the string contains any permutation of the pattern.

# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

#     abc
#     acb
#     bac
#     bca
#     cab
#     cba

# If a string has ‘n’ distinct characters it will have n!n!n! permutations.

# Example 1:

# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.

# Example 2:

# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in the given string as a substring.

# Example 3:

# Input: String="bcdxabcdy", Pattern="bcdyabcdx"
# Output: true
# Explanation: Both the string and the pattern are a permutation of each other.

# Example 4:

# Input: String="aaacb", Pattern="abc"
# Output: true
# Explanation: The string contains "acb" which is a permutation of the given pattern.

def food_permutation(str, pattern):
    chars = {}
    start = 0
    for char in pattern:
        if char not in chars:
            chars[char] = 0
        chars[char] -= 1

    for end in range(len(str)):
        if str[end] not in chars:
            chars[str[end]] = 0
        chars[str[end]] += 1
        if chars[str[end]] == 0:
            del chars[str[end]]

        if end - start + 1 != len(pattern):
            continue

        if len(chars) == 0:
            return True

        if str[start] not in chars:
            chars[str[start]] = 0
        chars[str[start]] -= 1
        if chars[str[start]] == 0:
            del chars[str[start]]
        start += 1
    return False

# examples = [
#         ["oidbcaf", "abc"],
#         ["odicf", "dc"],
#         ["bcdxabcdy", "bcdyabcdx"],
#         ["aaacb", "abc"]
#     ]
# for example in examples:
#     print(food_permutation(*example))




# String Anagrams (hard) #

# Given a string and a pattern, find all anagrams of the pattern in the given string.

# Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

#     abc
#     acb
#     bac
#     bca
#     cab
#     cba

# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

# Example 1:

# Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

# Example 2:

# Input: String="abbcabc", Pattern="abc"
# Output: [2, 3, 4]
# Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

def find_string_anagrams(str, pattern):
    chars = {}
    start = 0
    matches = 0
    res = []

    for char in pattern:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1

    for end in range(len(str)):
        if str[end] in chars:
            chars[str[end]] -= 1
        if chars[str[end]] == 0:
            matches += 1

        if end - start + 1 != len(pattern):
            continue

        if matches == len(chars):
            res.append(start)

        if str[start] in chars:
            if chars[str[start]] == 0:
                matches -= 1
            chars[str[start]] += 1
        start += 1

    return res

# print(find_string_anagrams("ppqp", "pq"))
# print(find_string_anagrams("abbcabc", "abc"))


"""
Smallest Window containing Substring (hard) #

Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

Example 2:

Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters of the pattern is "abc".

Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
"""

def find_substring(str, pattern):
    chars = {}
    start = 0
    matches = 0
    min_length = len(str) + 1
    substring_idx = len(str)

    for char in pattern:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1
    
    for end in range(len(str)):
        if str[end] in chars:
            chars[str[end]] -= 1
            if chars[str[end]] == 0:
                matches += 1

        while matches == len(chars):
            if str[start] in chars:
                if chars[str[start]] == 0:
                    matches -= 1
                chars[str[start]] += 1
            start += 1
        
            if end - start + 1 < min_length:
                substring_idx = start
                min_length = end - start + 1

    return str[substring_idx:substring_idx+min_length+1]

# print(find_substring("aabdec", "abc"))
# print(find_substring("abdabca", "abc"))
# print(find_substring("adcad", "abc"))

"""
Words Concatenation (hard) #

Given a string and a list of words, find all the starting indices of substrings in 
the given string that are a concatenation of all the given words exactly once without
any overlapping of words. It is given that all words are of the same length.

Example 1:

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".

Example 2:

Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".
"""

def find_word_concatenation(str, words):
    word_freqs = {}
    word_length = len(words[0])
    res = []
    
    for word in words:
        if word not in word_freqs:
            word_freqs[word] = 0
        word_freqs[word] += 1

    for i in range(0, len(str) - len(words) * word_length + 1):
        words_seen = {}
        for j in range(0, len(words)):
            idx = i + word_length * j
            word = str[idx:idx+word_length]

            if word not in word_freqs:
                break

            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            if words_seen[word] > word_freqs[word]:
                break
            
            if j == len(words) -1:
                res.append(i)
            
    return res

print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))

2