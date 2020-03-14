#!/usr/bin/env python3

# Given a string, return a new string made of every other char starting with
# the first, so "Hello" yields "Hlo".

# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello

def string_bits(s):
    return s[::2]
print(string_bits('Hello'))

def string_bits_1(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i]
    return result
print(string_bits_1("Andromeda"))