#!/usr/bin/env python3

# Given a string, return a new string made of 3 copies of the last 2
# chars of the original string, the string length will be atleast 2

# extra_end('Hello') → 'lololo'
# extra_end('ab') → 'ababab'
# extra_end('Hi') → 'HiHiHi'

def extra_end(s):
    return s[-2:] * 3

print(extra_end('Hello'))
