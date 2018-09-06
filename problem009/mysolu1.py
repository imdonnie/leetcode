import sys
import operator
class Solution:
    def isPalindrome(self, x):
        num_list = list(str(x))
        r_num_list = num_list.copy()
        num_list.reverse()
        print(num_list)
        print(r_num_list)
        return operator.eq(num_list, r_num_list)
        
if __name__ == '__main__':
    input_str = int(sys.argv[1])
    solution = Solution()
    result = solution.isPalindrome(input_str)
    print(result)