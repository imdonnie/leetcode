import argparse
import sys

# list.index has several option args
# including 'beg', which decides where the function begins
# the following use of list.index has 'beg=index_1+1', to avoid getting the same index as i

class Solution:
	def twoSum(self, nums, target):
		for i in range(len(nums)):
			if target - nums[i] in nums[i+1:]:			
				return i, list.index(nums, target - nums[i], i+1)

if __name__ == '__main__':

	nums = sys.argv[1].split(',')
	nums = list(map(int, nums))
	target = int(sys.argv[2])

	solution = Solution()
	result = solution.twoSum(nums, target)
	print(result)