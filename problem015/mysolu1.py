import sys

import operator
class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        print(nums)
        result = []
        if operator.eq(nums, []):
            return []
        if nums[0] > 0 or nums[-1] < 0:
            return []
        for i, num in enumerate(nums):
            if i == 0 or nums[i] > nums[i-1]:
                left_p = i + 1
                right_p = len(nums) - 1

                # print('i:{0}\tl:{1}\tr:{2}\t {3}\t{4}\t{5}'.format(nums[i], nums[left_p], nums[right_p], i, left_p, right_p))
                while left_p < right_p:
                    print('i:{0}\tl:{1}\tr:{2}\t {3}\t{4}\t{5}'.format(nums[i], nums[left_p], nums[right_p], i, left_p, right_p))

                    # 核心逻辑：双指针向中间逼近，遇到符合条件就添加
                    # 若<0，说明当前值不足，左值过小，因此左指针向右移动；若>0，说明当前值超出，右值过大，因此右指针向左移动
                    sum_3 = nums[i] + nums[left_p] + nums[right_p]
                    if sum_3 == 0:
                        result.append([nums[i], nums[left_p], nums[right_p]])
                        left_p += 1
                        right_p -= 1
                        # 去重
                        while nums[left_p] == nums[left_p - 1] and left_p < right_p:
                            left_p += 1
                        while nums[right_p] == nums[right_p + 1] and left_p < right_p:
                            right_p -= 1
                    if sum_3 < 0:
                        left_p += 1
                    elif sum_3 > 0:
                        right_p -= 1
        return result

if __name__ == '__main__':
    s = [-1,0,1,2,-1,-4]
    solution = Solution()
    result = solution.threeSum(s)
    print(result)