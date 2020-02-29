#!/usr/bin/env python3

#Given a string, return a string made of its first two chars, so the
# String "Hello" yeids "He".
# If the string is shorter than 2, return whatever there is,
# so "X" yeils "X", and empty string "" yeilds the
# empty string "".

# first_two('Hello') → 'He'
# first_two('abcdefg') → 'ab'
# first_two('ab') → 'ab'

def first_two(strn):
    return strn[:2]

print(first_two('abcdefg'))
    
