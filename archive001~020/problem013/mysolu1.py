# 时间复杂度O(n2)
import sys

class Solution:
    def romanToInt(self, s):
        if len(s) == 0:
            return 0
        result = 0
        s = s.replace('CM', ',900').replace('CD', ',400').replace('XC', ',90').replace('XL', ',40').replace('IX', ',9').replace('IV', ',4')
        s = s.replace('M', ',1000').replace('D', ',500').replace('C', ',100').replace('L', ',50').replace('X', ',10').replace('V', ',5').replace('I', ',1')
        print(s)
        s = s.strip().split(',')
        for char in s :
            if len(char) == 0:
                result = result
            else:
                result += int(char)
                print(result)
        return result

if __name__ == '__main__':
    s = sys.argv[1]
    solution = Solution()
    result = solution.romanToInt(s)
    print(result)