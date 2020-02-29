#!/usr/bin/env python3

# Given a String, a "a rotated left 2" verison where the first 2 chars
# are moved to the end. The string length will be at least 2.

# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'

def left2(s):
    return s[2:] + s [:2]

print(left2('java'))