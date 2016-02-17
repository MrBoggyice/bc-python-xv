'''
	the function twosum returns the index of two numbers provided 
	the two numbers are equal to the target which is the second parameter 
	in the function.
	
	so, the latter is much more better than the present twosum which is 
	basically explained and written for a layman to understand.

'''

def twosum(nums, target):
	index_list = range(len(nums))
	for idx in index_list:
		first_num =nums[idx]
		for  idx_j in range(idx + 1, len(nums)):
			second_num = nums [idx_j]
			num_sum = first_num + second_num
			if target == num_sum:
				return [idx, idx_j]

	return 'not found'


def twosumO(nums, target):
	for i in nums:
		for j in nums:
			if j+i == target:
				return [nums.index(i), nums.index(j)]

print twosumO([2, 5, 1, 7], 8)