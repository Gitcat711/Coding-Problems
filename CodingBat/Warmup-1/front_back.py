#!/usr/bin/env python3

#Given a string, return a string where a
# first and last chars #has been exchnaged

# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(s):
    if len(s) <= 1:
        return s

    return s[len(s) - 1] + s[1:len(s) - 1] + s[0]

print(front_back('code'))
