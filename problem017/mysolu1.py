import sys

import operator
class Solution:
    def letterCombinations(self, digits):
        result = []
        digit_chars_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        num_1 = digits[0]
        num_2 = digits[1]
        chars_1 = digit_chars_map[num_1]
        chars_2 = digit_chars_map[num_2]
        for i in range(len(chars_1)):
            for j in range(len(chars_2)):
                comb = chars_1[i]+chars_2[j]
                print(comb)
                result.append(comb)
        return result



if __name__ == '__main__':
    s = sys.argv[1]
    solution = Solution()
    result = solution.letterCombinations(s)
    print(result)