#!/usr/bin/env python3

# Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there. Return
# a new string which is 3 copies of the front.

# front3('Java') → 'JavJavJav'
# front3('Chocolate') → 'ChoChoCho'
# front3('abc') → 'abcabcabc'

def front3(strn):
    front = strn[0:3]
    return 3 * front

print(front3('Java'))

def front_3(s):
  # Figure the end of the front
    front_end = 3
    if len(s) < front_end:
        front_end = len(s)
    front = s[:front_end]
    return front + front + front        
print(front3('Chocolate'))