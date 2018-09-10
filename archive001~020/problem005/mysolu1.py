import argparse
import sys

class Solution:	
	def longestPalindrome(self, s):
		s_list = list(s)
		# 判断整个字符串是否为回文串
		# 整个为回文串则全部返回，否则递归
		if self.isReverseString(s) == 0:
			return s
		else:
			head_result = self.withHead(s)
			tail_result = self.withTail(s)
			middle_result = self.longestPalindrome(''.join(s_list[1:-1]))
			# print("head_result:{0}, tail_result:{1}, middle_result:{2}".format(head_result, tail_result, middle_result))
			result_list = [head_result, tail_result, middle_result]
			len_list = list(map(len, result_list))
			max_index = len_list.index(max(len_list))
			return result_list[max_index]

	def withHead(self, s):
		s_list = list(s)
		tail = 0
		for i, _ in enumerate(s_list):
			if self.isReverseString(s_list[:i]) == 0:
				tail = i
		return ''.join(s_list[:tail])

	def withTail(self, s):
		s_list = list(s)
		head = len(s_list)
		for i, _ in enumerate(s_list):
			if self.isReverseString(s_list[len(s_list)-i:]) == 0:
				head = len(s_list)-i
		return ''.join(s_list[head:])

	def isReverseString(self, s):
		s_list = list(s)
		flag = 0
		# 判断整个字符串是否为回文串
		for i, _ in enumerate(s_list):
			if s_list[i] != s_list[len(s_list)-i-1]:
				flag = 1
				break
		if flag == 0:
			return 0
		else:
			return 1	
	def perfectReverse(self, s):
		s_list = list(s)
		flag = 0
		# 判断整个字符串是否为回文串
		for i, _ in enumerate(s_list):
			if s_list[i] != s_list[len(s_list)-i-1]:
				flag = 1
				break
		if flag == 0:
			return s
		else:
			return ''

if __name__ == '__main__':

	s = sys.argv[1]

	solution = Solution()
	result = solution.longestPalindrome(s)
	print(result)