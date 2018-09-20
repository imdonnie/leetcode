class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # hay_list = list(haystack)
        # needle_list = list(needle)
        entrance = i = j = 0
        flag = 0
        ln = len(needle)
        while i+ln <= len(haystack) :
            if haystack[i:i+ln] == needle:
                return i
            else:
                i += 1
        return -1

if __name__ == '__main__':
    hay = 'aab'
    needle = "ab"
    s = Solution()
    for i in range(1000):
        r = s.strStr(hay, needle)
    print(r)