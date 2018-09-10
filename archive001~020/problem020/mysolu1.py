import sys

import operator
class Solution:
    def isValid(self, s):
        stack = ['']
        left_half = ['(', '[', '{', '']
        right_half = [')', ']', '}', '']
        if s[0] in right_half or len(s) == 0:
            return False
        for char in s:
            print(char)
            if char in left_half:
                stack.append(char)
            elif char in right_half and left_half.index(stack[-1]) != right_half.index(char):
                return False
            elif char in right_half and left_half.index(stack[-1]) == right_half.index(char):
                stack.pop()
            print(stack)
        res = True if operator.eq(stack, ['']) else False
        return res

if __name__ == '__main__':
    s = sys.argv[1]
    solu = Solution()
    res = solu.isValid(s)
    print(res)