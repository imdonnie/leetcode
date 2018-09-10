class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        dic={")":"(","]":"[","}":"{"}
        for x in s:
            if x in dic.values():
                l.append(x)
            elif x in dic.keys():
                if l==[] or dic[x]!=l.pop():
                    return False
            else:
                return False
        return l==[]