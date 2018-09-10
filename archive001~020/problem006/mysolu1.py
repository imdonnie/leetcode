# 时间复杂度O(s*numRows)
import sys

class Solution:
    def convert(self, s, numRows):
        if len(s) == 0 or numRows == 1:
            return s

        # P     I     N     .     .
        # A   L S   I G   . .   . .
        # Y A   H R   . .   . .   .
        # P     I     .     .     .

        s_list = list(s)
        wall_height = numRows
        ladder_height = numRows-2
        duplicate_num = len(s)//(wall_height + ladder_height)
        tail_num = len(s)%(wall_height + ladder_height)
        row_list = []
        char_matrix = [[] for i in range(wall_height)]
        result_list = []
        for i, char in enumerate(s_list):
            small_i = i%(wall_height + ladder_height)
            row_num = (wall_height - 1) - abs(small_i - (wall_height - 1))
            row_list.append(row_num)
            char_matrix[row_num].append(char)
        for row in char_matrix:
            for char in row:
                result_list.append(char)
        return ''.join(result_list)
        

if __name__ == '__main__':
    s = sys.argv[1]
    n = int(sys.argv[2])
    solution = Solution()
    result = solution.convert(s, n)
    print(result)