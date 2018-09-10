import sys

import operator
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 设置一个“虚”头节点，便于处理边界情况
        # 一遍扫描就可以完成
        v_head = ListNode('head')
        v_head.next = head
        p_n = p_head = v_head
        for i in range(n):
            # print('{0}->{1}'.format(p_n.val, p_n.next.val)) 
            p_n = p_n.next
        while p_n.next:
            p_n = p_n.next
            p_head = p_head.next
        p_head.next = p_head.next.next
        return v_head.next