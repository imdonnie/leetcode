import argparse
import sys

class Solution:
	def findMedianSortedArrays(self, nums1, nums2):
		nums = nums1 + nums2
		nums.sort()
		length = len(nums)
		# index = (length-1)/2 if length % 2 != 0 else ((length/2)+(length/2)-1)/2
		if length % 2 != 0:
			index = int((length-1)/2)
			mid = nums[index]
		else:
			mid = (nums[int((length/2))]+nums[int((length/2)-1)])/2
		return int(mid)


if __name__ == '__main__':

	nums1 = list(map(int, sys.argv[1].split(',')))
	nums2 = list(map(int, sys.argv[2].split(',')))

	solution = Solution()
	result = solution.findMedianSortedArrays(nums1, nums2)
	print(result)