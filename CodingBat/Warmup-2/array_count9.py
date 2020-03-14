#!/usr/bin/env python3

# Given an aray of ints,
# Return number of 9's in the
# array.

# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(num_arr):
    count = 0
    for num in num_arr:
        if num == 9:
            count += 1
    return count

print(array_count9([1, 9, 9, 3, 9]))
