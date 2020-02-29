#!/usr/bin/env python3

# Given two Strings, a and b, return a string of the form short + long + short,
# with the shorter string on the outside and the longer string on the inside,
# The strings will not be the same length, but the maybe empty(len == 0)

# combo_string('Hello', 'hi') → 'hiHellohi'
# combo_string('hi', 'Hello') → 'hiHellohi'
# combo_string('aaa', 'b') → 'baaab'

def combo_string(a, b):
    s = a
    l = b
    if len(s) > len(l):
        s, l = l, s
    return s + l + s

print(combo_string('Hello', 'hi'))

        
