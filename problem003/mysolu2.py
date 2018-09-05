import argparse
import sys

# list.index has several option args
# including 'beg', which decides where the function begins
# the following use of list.index has 'beg=index_1+1', to avoid getting the same index as i

class Solution:
	def lengthOfLongestSubstring(self, s):
		if len(s) == 0:
			return 0
		else:
			str_list = list(s)
			max_list = []
			for start, char in enumerate(str_list):	
				left_length = len(str_list[start:])
				print(start)		
				for i, char in enumerate(str_list[start+1:]):
					print("current char:{0}\t current forstring:{1}".format(char, str(str_list[start:i+start+1])))
					if char in str_list[start:i+start+1]:
						left_length = i + 1 - 0
						break;
				max_list.append(left_length)
		print(max_list)
		return max(max_list)

if __name__ == '__main__':

	# s = sys.argv[1]
	s = 'asvndsvin aeifnwe'
	solution = Solution()
	result = solution.lengthOfLongestSubstring(s)
	print(result)