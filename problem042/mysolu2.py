import sys
import operator
class Solution:
	def trap(self, height):
		if operator.eq(height, []):
			return 0

		height_list = list(height)
		max_height = max(height_list)
		max_height_index = height_list.index(max_height)
		left_p = 0
		right_p = len(height_list)-1

		left_area = right_area = 0
		left_max = right_max = 0

		while left_p < max_height_index:
			current_height = height_list[left_p]
			if  current_height != 0:
				# 从当前的积水区域中减去新柱体阻隔的部分（包括该柱体本身）
				left_area -= min(left_max, current_height) * (max_height_index - left_p)
				# 计算当前柱体到最高柱体的局部面积
				p_area = (max_height_index - left_p - 1) * current_height
				# 更新积水区域
				left_area += p_area
				# print('{0} {1} {2}'.format(current_height, left_area, p_area))
				left_max = left_max if left_max >= current_height else current_height
			left_p += 1

		while right_p > max_height_index:
			current_height = height_list[right_p]
			if  current_height != 0:
				# 从当前的积水区域中减去新柱体阻隔的部分（包括该柱体本身）
				right_area -= min(right_max, current_height) * (right_p - max_height_index)
				# 计算当前柱体到最高柱体的局部面积
				p_area = (right_p - max_height_index - 1) * current_height
				# 更新积水区域
				right_area += p_area
				# print('{0} {1} {2}'.format(current_height, right_area, p_area))
				right_max = right_max if right_max >= current_height else current_height
			right_p -= 1		

		return right_area+left_area

if __name__ == '__main__':
	s = sys.argv[1].split(',')
	s = list(map(int, s))
	solution = Solution()
	result = solution.trap(s)
	print(result)