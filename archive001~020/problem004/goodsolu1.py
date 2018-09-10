import sys

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if (target - num) in dic:
                return i,dic[target - num]
            dic[num] = i

if __name__ == '__main__':

    nums = sys.argv[1].split(',')
    nums = list(map(int, nums))
    target = int(sys.argv[2])

    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)