# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_head = l1 if l1.val <= l2.val else l2
        print('here')
        while l1.next:
            while l2.next:
                print('l1:{0} l2:{1}'.format(l1.val, l2.val))
                l2 = l2.next
            l1 = l1.next
                # if l2.val >= l1.val and l2.val <= l1.next.val:
                #     new_l1_next = ListNode(l2.val)
                #     new_l1_next.next = l1.next
                #     l1.next = new_l1_next
                #     l2 = l2.next
                # else:
                #     l1 = l1.next
        return new_head