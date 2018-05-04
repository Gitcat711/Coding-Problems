
#2. Given an array of ints, return True if the array is length 1 or more,
# and the first element and the last element are equal.
		#same_first_last([1, 2, 3]) → False
		#same_first_last([1, 2, 3, 1]) → True
		#same_first_last([1, 2, 1]) → True
#Hint: The length is nums.length, the first element is nums[0] and the 
#last element is nums[nums.length - 1]

def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[-1]


