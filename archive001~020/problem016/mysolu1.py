import sys

import operator
class Solution:
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        min_diff = float("inf")
        print('{0}\t{1}'.format(str(nums), target))
        result = []
        if operator.eq(nums, []):
            return []
        for i, num in enumerate(nums):
            if i == 0 or nums[i] > nums[i-1]:
                left_p = i + 1
                right_p = len(nums) - 1

                # print('i:{0}\tl:{1}\tr:{2}\t {3}\t{4}\t{5}'.format(nums[i], nums[left_p], nums[right_p], i, left_p, right_p))
                while left_p < right_p:
                    # 核心逻辑：双指针向中间逼近，遇到符合条件就添加
                    # 若<0，说明当前值不足，左值过小，因此左指针向右移动；若>0，说明当前值超出，右值过大，因此右指针向左移动
                    current_sum = nums[i] + nums[left_p] + nums[right_p]
                    current_diff = abs(nums[i] + nums[left_p] + nums[right_p] - target)
                    # print('i:{0}\tl:{1}\tr:{2}\t {3}\t{4}\t{5}'.format(nums[i], nums[left_p], nums[right_p], min_diff, current_sum, current_diff))
                    if current_diff < min_diff:
                        min_diff = current_diff
                        result =[nums[i], nums[left_p], nums[right_p]]

                    if current_sum <= target:
                        left_p += 1
                    elif current_sum > target:
                        right_p -= 1
        return sum(result)

if __name__ == '__main__':
    s = [1,1,1,1]
    target = 0
    solution = Solution()
    result = solution.threeSumClosest(s, target)
    print(result)