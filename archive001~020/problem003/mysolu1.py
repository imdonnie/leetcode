import argparse
import sys

# list.index has several option args
# including 'beg', which decides where the function begins
# the following use of list.index has 'beg=index_1+1', to avoid getting the same index as i

# 动态规划解法（虽然结果并不好）
# 接单分析，题目要求寻找一个字符串的最长连续子串的长度，分析可知，最大值=max{包含开头的，包含末尾的，两侧都不含的}
class Solution:
	def lengthOfLongestSubstring(self, s):
		if len(s) == 0:
			return 0
		else:
			str_list = list(s)
			left_length = len(str_list)
			right_length = len(str_list)
			middle_length = len(str_list)
			for i, char in enumerate(str_list[1:]):
				print("current char:{0}\t current forstring:{1}".format(char, str(str_list[0:i+1])))
				if char in str_list[0:i+1]:
					left_length = i + 1 - 0
					break;
			print(left_length)

			for i, char in enumerate(str_list[:-1]):
				print("current char:{0}\t current forstring:{1}".format(str_list[len(str_list)-i-2], str(str_list[-i-1:])))
				if str_list[len(str_list)-i-2] in str_list[-i-1:]:
					right_length = i + 1 - 0
					break;
			print(right_length)

			str_list = str_list[1:-1]	
			middle_length = self.lengthOfLongestSubstring(''.join(str_list))
			result_list = [left_length, right_length, middle_length]
			print("current string:{0}\t result:{1}".format(str(s), str(result_list)))
			return max(result_list)

if __name__ == '__main__':

	s = sys.argv[1]
	solution = Solution()
	result = solution.lengthOfLongestSubstring(s)
	print(result)