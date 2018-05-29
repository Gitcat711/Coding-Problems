#! /usr/bin/env python3
def find_in_sorted(nums, target):
    start, end = 0, len(nums) - 1
    while start < end:
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

assert find_in_sorted([], 0) == -1
assert find_in_sorted([1,2,3], 0) == -1
assert find_in_sorted([1,2,3], 2) == 1
print("All Passes")


