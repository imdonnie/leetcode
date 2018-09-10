class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num_1 = 0
        num_2 = 0
        time = 0
        raw_sum_list = []
        while l1 or l2:
            val_1 = l1.val if l1 != None else 0
            val_2 = l2.val if l2 != None else 0
            raw_sum_list.append(val_1 + val_2)
            l1 = l1.next if l1 != None else l1
            l2 = l2.next if l2 != None else l2
        # raw_sum_list.reverse()
        for i, raw_sum in enumerate(raw_sum_list[:-1]):
            raw_sum_list[i+1] = raw_sum_list[i+1]+raw_sum_list[i]//10
            raw_sum_list[i] = raw_sum_list[i]%10
        if raw_sum_list[-1] >= 10:
            res_1 = raw_sum_list[-1]//10
            res_2 = raw_sum_list[-1]-10
            raw_sum_list.pop()
            raw_sum_list.append(res_2)
            raw_sum_list.append(res_1)
        return raw_sum_list