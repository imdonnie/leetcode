# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        v_head = ListNode('head')
        v_head.next = head
        count = 0
        p = v_head
        while p and p.next:
            # print('{0}->{1}->{2}'.format(p.val, p.next.val, p.next.next.val))
            p_n = p.next
            if p.next.next is None:
                return v_head.next
            else:
                p.next = p_n.next
                p_n.next = p.next.next
                p.next.next = p_n          
                p = p.next.next if p.next.next else p
        return v_head.next