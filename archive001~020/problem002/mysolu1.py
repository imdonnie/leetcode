import sys

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
        while l1 != None:
            num_1 = num_1 + l1.val*(10**time)
            time = time + 1
            l1 = l1.next
        time = 0
        while l2 != None:
            num_2 = num_2 + l2.val*(10**time)
            time = time + 1
            l2 = l2.next
        num_sum = num_1 + num_2
        sum_list = list(str(num_sum))
        sum_list.reverse()
        return list(map(int, sum_list))

if __name__ == '__main__':

	l1 = list(map(int, sys.argv[1].split(',')))
	l2 = list(map(int, sys.argv[2].split(',')))

	solution = Solution()
	result = solution.addTwoNumbers(l1, l2)
	print(result)