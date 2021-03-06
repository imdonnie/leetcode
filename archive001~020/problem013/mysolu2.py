# 时间复杂度O(n)
import sys

class Solution:
    def romanToInt(self, s):
        if len(s) == 0:
            return 0
        char_1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        char_2 = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        i = 0
        result = 0
        while i < len(s):
            if s[i:i+2] in char_2:
                result += char_2[s[i:i+2]]
                i += 2
            else:
                result += char_1[s[i]]
                i += 1
        return result

if __name__ == '__main__':
    s = sys.argv[1]
    solution = Solution()
    result = solution.romanToInt(s)
    print(result)