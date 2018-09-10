import argparse
import sys

class Solution:
	def lengthOfLongestSubstring(self, s):
		str_list = list(s)
		length = len(str_list)
		if length == 0:
			return 0
		slow_p = fast_p = 0
		result = 1
		while slow_p < length-1 and fast_p < length-1:
			sub_str_list = str_list[slow_p:fast_p+1]
			temp = len(sub_str_list)
			print("current char:{0}\t current sub:{1}".format(str_list[fast_p+1], str(sub_str_list)))
			if not str_list[fast_p+1] in sub_str_list:
				fast_p = fast_p + 1
				temp = temp + 1
			else:
				slow_p = slow_p + 1
			result = result if result >= temp else temp
		return result

if __name__ == '__main__':

	s = sys.argv[1]
	# s = 'asvndsvin aeifnwe'
	solution = Solution()
	result = solution.lengthOfLongestSubstring(s)
	print(result)