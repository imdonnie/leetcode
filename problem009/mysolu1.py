import sys
import re
class Solution:
    def isPalindrome(self, x):
        num_list = list(str(x))
        return num_list
        
if __name__ == '__main__':
    str = int(sys.argv[1])
    solution = Solution()
    result = solution.myAtoi(str)
    print(result)