#!/usr/bin/env python3

# Given 3 int values, a, b, c, return their sum. However, of one of the values
# is the same as other, then it won't count towards sum.

def lone_sum(a,b,c):
    s = 0
    if a != b and a !=c:
        s += a

    if b !=a and b !=c :
        s+=b

    if c != a and c !=b:
        s+=c

    return s

print(lone_sum(5,6,7))
