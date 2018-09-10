import sys
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def generateParenthesis(self, n):
        n = int(n)
        all_res = set()
        res = set()
        if n == 0:
            return res
        else:
            res.add('()')
            all_res.add('()')
        for i in range(1, n):
            old_res = list(res)
            options = []
            for j in res:
                for pos_1 in range(len(j)):
                    for pos_2 in range(pos_1, len(j)):
                        # print('{0}-{1}'.format(pos_1, pos_2))
                        # print('res:{0}\tp1-p2:{1}'.format(str(res), j[pos_1:pos_2+1]))
                        if j[pos_1:pos_2+1] in all_res:
                            new_opt = j[:pos_1]+'('+j[pos_1:pos_2]+')'+j[pos_2:]
                            # print('{0}-{1}:{2}\tnew_opt:{3}'.format(pos_1, pos_2, j[pos_1:pos_2+1], new_opt))
                            options.append(new_opt)
                            options.append('()'+j)
                            options.append(j+'()')
            for old in old_res:
                res.remove(old)
            for opt in options:
                all_res.add(opt)
                res.add(opt)
        return list(res)
if __name__ == '__main__':
    s = int(sys.argv[1])
    solu = Solution()
    res = solu.generateParenthesis(s)
    print(res)