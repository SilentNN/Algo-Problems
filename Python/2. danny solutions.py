"""
Given an array of positive numbers and a positive number ‘k’, find the maximum 
sum of any contiguous subarray of size ‘k’.
"""
from typing import *
from collections import deque
def findMaxSumSubArray(k: int, nums: List[int]) -> int:
	start = 0
	end = k
	max_sum = current_sum = sum(nums[start:end])
	while end < len(nums):
		current_sum = current_sum - nums[start] + nums[end]
		max_sum = max(current_sum, max_sum)
		start += 1
		end += 1
	return max_sum

# print(findMaxSumSubArray(3, [2, 1, 5, 1, 3, 2]))
# #9
# print(findMaxSumSubArray(2, [2, 3, 4, 1, 5]))
# #7


"""
Given an array of positive numbers and a positive number ‘S’, find 
the length of the smallest contiguous subarray whose sum is greater than 
or equal to ‘S’. Return 0, if no such subarray exists.
"""
def findMinSubArray(s: int, nums: List[int]) -> int:
	min_subarray_len = float('inf') 
	cur_subarray_len = 1
	start = 0
	end = 1
	current_sum = nums[0]
	if current_sum > s:
		min_subarray_len = min(cur_subarray_len,min_subarray_len)

	while end < len(nums):
		while current_sum <= s and end < len(nums):
			end += 1
			cur_subarray_len += 1
			current_sum += nums[end - 1]
			if current_sum >= s:
				min_subarray_len = min(cur_subarray_len,min_subarray_len)
		while current_sum >= s:
			current_sum -= nums[start]
			start += 1
			cur_subarray_len -= 1
			if current_sum >= s:
				min_subarray_len = min(cur_subarray_len,min_subarray_len)

	return min_subarray_len

# print(findMinSubArray(7, [2, 1, 5, 2, 3, 2]))
# print(findMinSubArray(7, [2, 1, 5, 2, 8]))
# print(findMinSubArray(8, [3, 4, 1, 1, 6]))

"""
Given a string, find the length of the longest substring 
in it with no more than K distinct characters.
"""

def findLength(char_str: str, k: int) -> int:
	start = 0
	end = 0
	cur_substring = 0
	max_substring = float('-inf')
	my_set = set()

	while end < len(char_str):
		end += 1
		new_char = char_str[end-1]
		if new_char not in my_set:
			my_set.add(new_char)
			cur_substring += 1
		
		if cur_substring <= k:
			max_substring = max(max_substring, cur_substring)
		while cur_substring <= k and start < len(char_str) -1:
			if char_str[start] in my_set:
				my_set.remove(char_str[start])
				cur_substring -= 1
			start += 1
		
	return max_substring

# print(findLength('araaci', 2))
# print(findLength('araaci', 1))
# print(findLength('cbbebi', 3))

"""
Given an array of characters where each character represents a fruit tree, 
you are given two baskets and your goal is to put maximum number of fruits 
in each basket. The only restriction is that each basket can have only 
one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. 
You will pick one fruit from each tree until you cannot, i.e., you will stop 
when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.
"""

def findLegnth(fruit: List[str]) -> int:
	end = 0
	fruit_set = set()
	set_size = 0
	basket_size = 0
	while end < len(fruit):
		end += 1
		new_fruit = fruit[end-1]
		if new_fruit in fruit_set:
			basket_size += 1
		#new fruit 
		elif set_size < 2:
			set_size += 1
			fruit_set.add(new_fruit)
			basket_size +=1
		elif set_size == 2:
			fruit_set.add(new_fruit)
			#determine new start to get new basket_size
			new_start = end - 2
			while fruit[new_start] == new_fruit:
				new_start -= 1
			other_fruit = fruit[new_start]
			while fruit[new_start] in (other_fruit, new_fruit):
				new_start -= 1
			basket_size = end - new_start - 1
			fruit_set.remove(fruit[new_start])
			print("new_start: {}".format(new_start))
			print("other_fruit: {}".format(other_fruit))
		else:
			basket_size = -1
		print("end: {}".format(end))
		print(fruit_set)
		print('basket_size: {}'.format(basket_size))

	return basket_size



# print(findLegnth(['A', 'B', 'C', 'A', 'C']))
"""		             o     n    e
set_size = 2
set = {b, c, a}
basket_size = 2
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the 
subarray ['C', 'A', 'C']
"""
# print(findLegnth(['A', 'B', 'C', 'B', 'B', 'C']))
"""
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""


"""
Given a string, find the length of the longest substring
which has no repeating characters.
"""

def findLength(char_str: str) -> int:
	start = 0
	end = 0
	str_len = len(char_str)
	if str_len < 1:
		return str_len
	start = 0
	end = 1
	cur_longest = 1
	max_longest = 1
	while end < str_len:
		old_end_char = char_str[end - 1]
		end += 1
		new_char = char_str[end - 1]
		#if you find a repeat, start a new window
		if old_end_char == new_char:
			start = end -1
			cur_longest = 1
		else:
			cur_longest += 1
		print("start: {}".format(start))
		print("end: {}".format(end))
		print("cur_longest: {}".format(cur_longest))
		max_longest = max(max_longest, cur_longest)
		print("max_longest: {}".format(max_longest))
	return max_longest


# print(findLength('aabccbb'))
# print(findLength('abbbb)'))
# print(findLength('abccde'))

"""
Given an array containing 0s and 1s, if you are allowed to replace no more 
than ‘k’ 0s with 1s, find the length of the longest contiguous subarray 
having all 1s.
"""
def findLength(int_list: List[int], k: int) -> int:
	start = end = 0
	cur_subarray = max_subarray = 0
	cur_k = k
	while end < len(int_list):
		end += 1
		new_int = int_list[end -1]
		if new_int == 1:
			cur_subarray += 1
		elif new_int == 0 and cur_k > 0:
			cur_k -= 1
			cur_subarray += 1
		elif new_int == 0 and cur_k == 0:
			while int_list[start] == 1:
				start += 1
			start += 1
			cur_subarray = end - start
		max_subarray = max(cur_subarray, max_subarray)
	return max_subarray

# print(findLength([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2))
# print(findLength([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3))

"""
0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1
            s     e
f

k: 0
max_subarray: 4
cur_subarray: 4

increment e forward until we use up all k's
when we have no more k's and we need to move the k, we slide start until we recover
the k
	recalculate the cur_subarray
"""


"""


Given a string and a pattern, find out if the string contains any permutation of the 
pattern.

Permutation is defined as the re-arranging of the characters of the string. 
For example, “abc” has the following six permutations:

    abc
    acb
    bac
    bca
    cab
    cba

If a string has ‘n’ distinct characters it will have n!n!n! permutations.

'oidacafabc', 
    s  
       e

'abc'
 111
letter_count: 3

if end encounters a letter not in the dict:
	move start to end to the next letter
	restart_dict and letter_count
if letter_count is set to zero:
	set permutation_found
if letter allocation nonzero:
	decrement letter allocation.
	decrement letters_count
when letter allocation is zero: 
	move start up forward, refilling all letter allocations 
	and letter_count until we refill needed letter



"""
def findPermutation(check_string: str, pattern: str) -> bool: 
	letter_dict = {}
	for c in pattern:
		if c not in letter_dict:
			letter_dict[c] = 1
		else:
			letter_dict[c] += 1
	current_dict = letter_dict.copy()
	letter_count = len(pattern)
	cur_count = letter_count
	start = end = 0
	while end < len(check_string):
		end += 1
		new_char = check_string[end -1]
		if  new_char not in letter_dict:
			start = end
			current_dict = letter_dict.copy()
			cur_count = letter_count
		# letter part of pattern
		elif current_dict[new_char] > 0:
			current_dict[new_char] -= 1
			cur_count -= 1
		elif current_dict[new_char] == 0:
			while current_dict[new_char] == 0:
				current_dict[check_string[start]] += 1
				letter_count += 1
				start += 1
			current_dict[new_char] -= 1
			cur_count -= 1

		# print("start: {}".format(start))
		# print("end: {}".format(end))
		# print("cur_count: {}".format(cur_count))
		# print("current_dict: {}".format(current_dict))
		if cur_count == 0:
			return True

	return False

# print(findPermutation('oidbcaf', 'abc'))
# print(findPermutation('bcdxabcdy', 'bcdyabcdx'))
# print(findPermutation('aaacb', 'abc'))
# print(findPermutation('odicf', 'dc'))

"""
Given a string and a pattern, find all anagrams of the pattern in the given string.

Anagram is actually a Permutation of a string. For example, “abc” has the 
following six anagrams:

    abc
    acb
    bac
    bca
    cab
    cba

Write a function to return a list of starting indices of the anagrams of 
the pattern in the given string.

ppqap
    s
    e

pq
00

indices = []

increment end
	if item not in dict:
		restore dict
		restore allocation_count
		move start to end

	if item in dict and there is an allocation
		decrement value
	if item in dict and there is no allocation
		move start, restoring allocation until you reach new item
			move start past item
	if allocation_count == 0:
		add start to indices
		restore dict
		restore allocation_count
		move start to end
return indices

"""
def findStringAnagrams(chars: str, pattern: str) -> List[int]:
	start = end = 0
	indices = []
	allocation = len(pattern)
	pattern_dict = {}
	for c in pattern:
		if c not in pattern_dict:
			pattern_dict[c] = 1
		else:
			pattern_dict[c] += 1
	cur_dict = pattern_dict.copy()
	cur_allocation = allocation

	while end < len(chars):
		end += 1
		new_char = chars[end-1]
		if new_char not in cur_dict:
			cur_dict = pattern_dict.copy()
			cur_allocation = allocation
			start = end
		#new_char part of anagram chars
		elif cur_dict[new_char] > 0:
			cur_dict[new_char] -= 1
			cur_allocation -= 1
		elif cur_dict[new_char] == 0:
			while chars[start] != new_char:
				cur_dict[chars[start]] += 1
				start += 1
				cur_allocation += 1
			start += 1
		if cur_allocation == 0:
			indices.append(start)
		
# 		print("start: {}".format(start))
# 		print("end: {}".format(end))
# 		print("cur_dict: {}".format(cur_dict))
# 		print("cur_allocation: {}".format(cur_allocation))
	return indices


# print(findStringAnagrams('ppqp', 'pq'))
# print(findStringAnagrams('abbcabc', 'abc'))


"""
Smallest Window containing Substring (hard) #

Given a string and a pattern, find the smallest substring in the given 
string which has all the characters of the given pattern.

'zabbbadec', 
  s 
       e

'abc'
 001

increment end till we reach end of string
	check char at end-1
	if char not in dict and allocation_count is the original value:
		move start to end
	if char not in dict and allocation_count is not original value:
		do nothing, continue loop
	if char in dcit and there is an allocation for char:
		decrement allocation_count
		decrement char allocation in dict
		add to pattern_seen_set
	if char in dict and there is no allocation for char:
		copy pattern_seen_set to cur_pattern_seen_set
		set new_start = end-1
			decrement new_start until len(cur_pattern_seen_set) = 0
				if chars[new_star] in cur_pattern_sent_set:
					cur_pattern_seen_set.remove chars[new_start]
		if chars[start] == char: 
			increment start
		move start past char (restoring allocation and subtracting it as well)
	when allocation_count is zero, return string[start:end]




"""
def findSubstring(chars: str, pattern: str) -> str:
	start = end = 0
	char_dict = {}
	allocation_count = len(pattern)
	cur_allocation = allocation_count
	pattern_seen_set = set()
	for c in pattern:
		if c not in char_dict:
			char_dict[c] = 1
		else:
			char_dict[c] += 1
	while end < len(chars):
		end += 1
		new_char = chars[end-1]
		if new_char not in char_dict and cur_allocation == allocation_count:
			start = end
		elif new_char not in char_dict:
			pass
		elif new_char in char_dict and char_dict[new_char] > 0:
			char_dict[new_char] -= 1
			cur_allocation -= 1
			pattern_seen_set.add(new_char)
		elif new_char in char_dict and char_dict[new_char] == 0:
			cur_pattern_seen_set = pattern_seen_set.copy()
			new_start = end
			while len(cur_pattern_seen_set) > 0:
				new_start -= 1
				if chars[new_start] in cur_pattern_seen_set:
					cur_pattern_seen_set.remove(chars[new_start])
			start = new_start
		if cur_allocation == 0:
			return chars[start:end]
		print("start: {}".format(start))
		print("end: {}".format(end))
		print("cur_allocation: {}".format(cur_allocation))
		print("char_dict: {}".format(char_dict))
	return ""


# print(findSubstring('aabdec', 'abc'))
# print("*************")
# print(findSubstring('abdabca', 'abc'))
# print("*************")
# print(findSubstring('adcad', 'abc'))

"""
Given a string and a list of words, find all the starting indices of 
substrings in the given string that are a concatenation of all the 
given words exactly once without any overlapping of words. It is given 
that all words are of the same length.

'aaafoxcat', 
    s
       e

["cat", "fox"]
   0      0

prefix_dict:
	[1]: {"c", "f"}
	[2]: {"ca", "fo"}
	[3]: {"cat", "fox"}

allocation_count = 0

indices_list

while end < len(chars)
	increment end
	if chars[start:end] not in prefix_dict[len(chars[start:end])]:
		start = end
		reset allocation_count
		word_allocation
	if chars[start:end] in prefix_dict[len(chars[start:end])]:
		pass
	
	if chars[start:end] in word_dict:
		decrement word allocaiton
		decrement allocation count
		move start to end
	if allocation_count == 0: 
		append (end - char_catenation_count) to indices
		iterate backwards from end to find last used word
		add allocation
		increcrement allocation count
return indices
		



"""
def findWordConcatenation(chars: str, word_list: List[str]) -> List[int]:
	start = end = 0
	word_dict = {}
	max_word_len = 0
	total_word_len = 0
	for word in word_list:
		if word not in word_dict:
			word_dict[word] = 1
		else:
			word_dict[word] += 1
		max_word_len = max(max_word_len, len(word))
		total_word_len += len(word)
	prefix_dict = {}
	for i in range(1,max_word_len + 1):
		cur_set = set()
		for word in word_list:
			cur_set.add(word[0:min(i,len(word))])
		prefix_dict[i] = cur_set
	#print("word_dict: {}".format(word_dict))
	#print("total_word_len: {}".format(total_word_len))
	#print("prefix_dict: {}".format(prefix_dict))
	word_count = len(word_list)
	cur_count = word_count
	cur_word_dict = word_dict.copy()
	indices = []

	while end < len(chars):
		end += 1
		phrase = chars[start:end]
		if phrase not in prefix_dict[len(phrase)]:
			start = end
			cur_count = word_count
			cur_word_dict = word_dict.copy()
		# phrase is a prefix
		elif phrase in cur_word_dict and cur_word_dict[phrase] > 0:
			cur_word_dict[phrase] -= 1
			cur_count -= 1
			start = end
		elif phrase in cur_word_dict and cur_word_dict[phrase] == 0:
			start = end
			cur_count = word_count - 1
			cur_word_dict = word_dict.copy()
			cur_word_dict[phrase] -= 1
		
		if cur_count == 0:
			print("cur_word_dict: {}".format(cur_word_dict))
			print("cur_count: {}".format(cur_count))
			print("end: {}".format(end))
			indices.append(end - total_word_len)
			start = end
			cur_count = word_count - 1
			cur_word_dict = word_dict.copy()
			cur_word_dict[phrase] -= 1


	return indices

#print(findWordConcatenation('catfoxcat', ["cat", "fox"]))
print(findWordConcatenation('catcatfoxfox', ["cat", "fox"]))
