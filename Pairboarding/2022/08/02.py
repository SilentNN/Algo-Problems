# given a string, reverse the position of only the vowels

# example: "Hello World" --> "Hollo Werld"
# "Ee" --> "eE"

"""
initialize
    set with all vowels

iterate through string
    if a char is a vowel
        swap with last vowel of string (found via iterating backwards)
"""

def reverse_vowels(str): # "Hello World"
    vowels = {'a', 'e', 'i', 'o', 'u'}
    str_to_array = [*str]
    left_char_i = 0
    right_char_i = len(str) - 1

    while left_char_i < right_char_i: # 1 < 7
        left_char = str[left_char_i] # e
        right_char = str[right_char_i] # o

        if left_char.lower() in vowels:
            if right_char.lower() in vowels:
                str_to_array[left_char_i], str_to_array[right_char_i] = right_char, left_char # str[1], str[7] = 'o', 'e'
                left_char_i += 1
            right_char_i -= 1
        else:
            left_char_i += 1
        
    return ''.join(str_to_array)

print(reverse_vowels("Hello World"))
print(reverse_vowels("reverse all Of the VowEls"))
print(reverse_vowels("qweghryufiklasdfnb"))
print(reverse_vowels("acsdhafipocn"))