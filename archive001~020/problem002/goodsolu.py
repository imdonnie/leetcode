class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        sumlink = node = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            temp_node = ListNode((l1_val+l2_val+carry)%10)
            carry = (l1_val+l2_val+carry)//10
            node.next = temp_node
            node = node.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return sumlink.next