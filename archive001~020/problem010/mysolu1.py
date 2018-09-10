import sys
import re
class Solution:
    def isMatch(self, s, p):
        result = re.match(p, s)
        if result is None:
            return False
        result = result.group()
        print(result)
        if result == s:
            return True
        else:
            return False
        
if __name__ == '__main__':
    s = sys.argv[1]
    p = sys.argv[2]
    solution = Solution()
    result = solution.isMatch(s, p)
    print(result)