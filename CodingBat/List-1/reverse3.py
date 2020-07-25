#!/usr/bin/python3

#Given an array of ints length 3, return a new array 
#with the elements inn reverse order
#so {1, 2, 3} becomes {3, 2, 1}.
	#reverse3([1, 2, 3]) → [3, 2, 1]
	#reverse3([5, 11, 9]) → [9, 11, 5]
	#reverse3([7, 0, 0]) → [0, 0, 7]

def reverse1(nums):
    """
    Method1: reverse the elements in the list 
    """
    return nums[::-1]
print(reverse1([6,9,8]))

def reverse2(nums):
    """
    Method2: reverse the elements in the list 
    """
    return list(reversed(nums))
print(reverse2([5,4,6]))

def reverse3(nums):
    """
    Method3: reverse the elements in the list 
    """
    nums.reverse()
    return nums
print(reverse3([1,2,3]))