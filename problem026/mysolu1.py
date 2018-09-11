class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype:int
        """
        i = 0
        while i < len(nums):
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                nums.remove(nums[i])
            # print(nums)
            i += 1
        return len(nums)
        