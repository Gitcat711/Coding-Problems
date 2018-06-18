#! /usr/bin/env python3
vowels = "aeiou"

input_str = input("Enter the String: ")
# For caseless comparison, let's use casfold()
input_str = input_str.casefold()

#make a dictionary with each vowel a key and value-> 0
count = dict.fromkeys(vowels,0)

#count the vowels.
for char in input_str:
    if char in count:
        count[char] += 1

print(count)
