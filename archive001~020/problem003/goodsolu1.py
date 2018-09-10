import argparse
import sys

class Solution:
    def lengthOfLongestSubstring(self, s):
        left_flag = 0
        longest = 0
        hash_sub = dict()

        for i, char in enumerate(s):
            if (char in hash_sub) and (hash_sub[char] >= left_flag):
                longest = i - left_flag if i - left_flag > longest else longest
                left_flag = hash_sub[char] + 1
            hash_sub[char] = i
            print("left_flag:{0}\t hash_sub:{1} \tlongest:{2}".format(left_flag, str(hash_sub), longest))
        
        longest = len(s) - left_flag if len(s) - left_flag > longest else longest
        
        return longest

if __name__ == '__main__':

    s = sys.argv[1]
    # s = 'asvndsvin aeifnwe'
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)