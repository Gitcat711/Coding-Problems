#!/usr/bin/env python3

# Given a non-empty string like "Code" return
# a string like "CCoCodCode"

# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(s):
    result = ""
    # On each iteration, add the substring of the chars 0..i
    for i in range(len(s)):
        result = result + s[:i+1]
    return result

print(string_splosion("Kiron"))

def string_splosion_1(s):
    c = []
    for i in range(1, len(s) + 1):
        c.append(s[:i])
    return "".join(c)
print(string_splosion_1('Code'))