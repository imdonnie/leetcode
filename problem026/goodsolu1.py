class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        # nums >= 2
        index = 1
        pre = nums[0]
        for i in range(len(nums)):
            if pre != nums[i]:
                pre = nums[i]
                nums[index] = pre
                index += 1
        return index