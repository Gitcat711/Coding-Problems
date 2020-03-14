#!/usr/bin/env python3

# Given a string and a non-negative int n,
# we'll say that the front of the string is the first 3 chars,
# or whatever is there if the string is less than length 3.
# Return n copies of the front;

# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'


def front_times(s, n):
    return s[:3] * n
print(front_times('Chocolate', 2))

def front_times_1(s, n):
    front_len = 3
    if front_len > len(s):
        front_len = len(s)
    front = s[:front_len]

    result = ""
    for i in range(n):
        result += front
    return result
print(front_times_1('Abc', 3))