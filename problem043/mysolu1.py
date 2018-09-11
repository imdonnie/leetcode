class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return
        res = []
        q1, q2 = l1, l2
        while q1:
            res.append(q1)
            q1 = q1.next    
        while q2:
            res.append(q2) 
            q2 =q2.next         
        res = sorted(res, key=lambda x:x.val)
        return [i.val for i in res] 