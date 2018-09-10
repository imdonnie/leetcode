import argparse
import sys

class Solution:
	"""docstring for Solution"""
	def twoSum(self, nums, target):
		for i in range(len(nums)):
			# print(nums[i])
			for j in range(i + 1, len(nums)):	
				# print(nums[j])
				if nums[i]+nums[j] == target:
					return i, j

if __name__ == '__main__':

	nums = sys.argv[1].split(',')
	nums = list(map(int, nums))
	target = int(sys.argv[2])

	solution = Solution()
	result = solution.twoSum(nums, target)
	print(result)