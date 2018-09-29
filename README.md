# leetcode
2018.9.3~2018.9.10 : p001-p020

leetcode-30
import itertools
class Solution:
    
    def hasWord(self, s, word_list):
        for word in word_list:
            if s == word:
                return True
            
    def findSubstring(self, s, words):
        if s == '' or words == []:
            return []
        res = []
        mixed_words_list = list(map(lambda x:''.join(x), itertools.permutations(words)))
        max_len = len(mixed_words_list[0])
        ps = pe = 0
        while pe <= len(s):
            # print('{0}-{1}:{2}'.format(ps, pe, s[ps:pe]))
            if not self.hasWord(s[ps:pe], mixed_words_list):
                if len(s[ps:pe]) < max_len:
                    pe += 1
                else:
                    pe += 1
                    ps += 1
            else:
                res.append(ps)
                ps += 1
        return res
