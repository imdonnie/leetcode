import sys

class Solution:
    def trap(self, height):
        if len(height) == 0:
            return 0

        height_list = list(height)
        max_height = max(height_list)
        base_height = min(height_list)

        for i, _ in enumerate(height_list):
            height_list[i] -= base_height
        # 生成柱体结构
        sticks = []
        for h in height_list:
            sticks.append(self.getStick(h, max_height))
        # print('生成柱体')
        # print(sticks)    

        # 模拟全部落满水
        sticks = self.dropRain(sticks)
        # print('注水')
        # print(sticks)
        # 从左侧开始流出
        sticks = self.flowFromLeft(sticks)
        # print('左侧流出')
        # print(sticks)
        # 从右侧开始流出
        sticks = self.flowFromRight(sticks)
        # print('右侧流出')
        # print(sticks)
        # 统计剩余
        result = self.countUnit(sticks)
        # print('统计剩余')
        return result

    def getStick(self, height, max):
        stick = []
        for i in range(max):
            unit = 1 if i < height else 0
            stick.append(unit)
        return stick

    def dropRain(self, sticks):
        for i, stick in enumerate(sticks):
            for j, unit in enumerate(stick):
                stick[j] = -1 if unit != 1 else 1
        return sticks

    def flowFromLeft(self, sticks):
        for i, stick in enumerate(sticks):
            for j, unit in enumerate(stick):
                left_unit = sticks[i-1][j] if i >= 1 else 0
                right_unit = sticks[i+1][j] if i+1 < len(sticks) else 0
                # print('{} | {} | {}'.format(left_unit, unit, right_unit))
                stick[j] = stick[j] if left_unit != 0 and right_unit != 0 else self.convertUnit(stick[j])
        return sticks

    def flowFromRight(self, sticks):
        index_num = len(sticks)-1
        sticks.reverse()
        for i, stick in enumerate(sticks):
            for j, unit in enumerate(stick):
                # i = index_num - i
                left_unit = sticks[i-1][j] if i >= 1 else 0
                right_unit = sticks[i+1][j] if i+1 < len(sticks) else 0
                # print('{} | {} | {}'.format(left_unit, unit, right_unit))
                stick[j] = stick[j] if left_unit != 0 and right_unit != 0 else self.convertUnit(stick[j])
        sticks.reverse()
        return sticks

    def convertUnit(self, num):
        if num == 1:
            return 1
        elif num == -1 or num == 0:
            return 0

    def countUnit(self, sticks):
        count = 0
        for i, stick in enumerate(sticks):
            for j, unit in enumerate(stick):
                count = count+1 if unit == -1 else count
        return count

if __name__ == '__main__':
    s = sys.argv[1].split(',')
    s = list(map(int, s))
    solution = Solution()
    result = solution.trap(s)
    print(result)