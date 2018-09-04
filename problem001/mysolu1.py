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
		# for num in nums:
		# 	if (target - num) in nums and (target - num)!=num:
		# 		index_1 = nums.index(num)
		# 		index_2 = nums.index(target - num)
		# 		return index_1, index_2
		# 	else:
		# 		continue

if __name__ == '__main__':
	# parser = argparse.ArgumentParser(description='manual to this script')
	# parser.add_argument('--num', type=str, default = None)
	# parser.add_argument('--target', type=int, default=32)
	# args = parser.parse_args()

	nums = sys.argv[1].split(',')
	nums = list(map(int, nums))
	target = int(sys.argv[2])

	solution = Solution()
	result = solution.twoSum(nums, target)
	print(result)