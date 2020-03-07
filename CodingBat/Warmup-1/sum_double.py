#!/usr/bin/env python3

#Gven two int values, return their sum.
# Unless the two values are the same,
# then return double their sum.

# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

# Short
def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    return a + b
print(sum_double(2, 2))

# What Codingbat suggest
def sum_double_1(a, b):
    #Store the sum in a local variable.
    add = a + b
    # Double if both a & b are same.
    if a == b:
        add += add
    return add
print(sum_double_1(3, 2))