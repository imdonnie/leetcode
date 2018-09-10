import sys

import operator
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        digit2chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = [ i for i in digit2chars[digits[0]]]
        print(res)
        for i in digits[1:]:
            print('i:{0}, res:{1}, digit2chars[i]:{2}'.format(i, res, digit2chars[i]))
            res = [ m+n for m in res for n in digit2chars[i] ]
            print (res)
        return res   



if __name__ == '__main__':
    s = sys.argv[1]
    solution = Solution()
    result = solution.letterCombinations(s)
    print(result)