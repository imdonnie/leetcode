import sys

class Solution:
    def maxArea(self, height):
        i1 = 0
        i2 = len(height) - 1
        max_area = 0
        while i1 != i2:
            current_area = (i2-i1)*min(height[i1], height[i2])
            # print('{0}*{1}={2}'.format(height[i1], height[i2], current_area))
            max_area = current_area if current_area > max_area else max_area
            if height[i1] >= height[i2]:
                i2 -= 1
            else:
                i1 += 1
        return max_area
        
if __name__ == '__main__':
    s = sys.argv[1].split(',')
    s = list(map(int, s))
    solution = Solution()
    result = solution.maxArea(s)
    print(result)