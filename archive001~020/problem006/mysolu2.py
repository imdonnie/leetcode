import sys

class Solution:
    def convert(self, s, numRows):
        if len(s) == 0 or numRows == 1:
            return s

        s_list = list(s)                   # 字符串s拆分为list
        base_dict = {}                     # 用于存储每一行的基数
        base_list = []
        wall_height = numRows              # 竖排的“墙高”
        ladder_height = numRows-2          # 斜排的“梯长”
        unit_size = 2*wall_height - 2      # 基本单元大小
        duplicate_num = len(s)//unit_size  # 基本单元重复次数
        tail_num = len(s)%(unit_size)      # 末尾剩余元素
        row_list = []                      # 用于存储每个char所在的行号，规模=len(s)
        char_matrix = \
        [[] for i in range(wall_height)]   # 用于存储重排的char，规模=numRows*len(s)
        result_dict = {}                   # 用于存储最终结果
        result_list = []
        for i, char in enumerate(s_list):
            small_i = i%(unit_size)
            row_num = (wall_height - 1) - abs(small_i - (wall_height - 1))
            row_list.append(row_num)
            char_matrix[row_num].append(char)

        for i, row in enumerate(row_list):
            base_dict[row] = 1 if not row in base_dict else base_dict[row]+1

        base_list = list(base_dict.values())

        for i, char in enumerate(s_list):
            new_index = i + sum(base_list[:row_list[i]])
            print('{0}, {1}'.format(char, new_index))
            result_dict[new_index] = char
        for i in range(len(s_list)):
            # result_list.append(result_dict[i])
            print(result_dict[i])
        # for row in char_matrix:
        #     for char in row:
        #         result_list.append(char)
        return ''.join(result_list)
    

if __name__ == '__main__':
    s = sys.argv[1]
    n = int(sys.argv[2])
    solution = Solution()
    result = solution.convert(s, n)
    print(result)