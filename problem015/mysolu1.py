import sys

import operator
class Solution:
    def longestCommonPrefix(self, strs):
        if '' in strs:
            return ''
        if len(strs) == 0 or len(strs) == 1:
            return ''.join(strs)
        result = ''
        ss = min(strs, key=len)
        for s in strs:
            result = self.compareTwo(ss, s)
            ss = result
        return result

    def compareTwo(slef, str1, str2):
        result = ''
        loop_time = min(len(str1), len(str2)) + 1
        for i in range(loop_time):
            print('sub1:{0}, sub2:{1}'.format(str1[:i], str2[:i]))
            result = str1[:i] if operator.eq(str1[:i], str2[:i]) else result
        return result

if __name__ == '__main__':
    s = sys.argv[1].split(',')
    solution = Solution()
    result = solution.longestCommonPrefix(s)
    print(result)