import sys

class Solution:
    def intToRoman(self, num):
        num = int(num)

        if num == 0 or num > 3999:
            return ''

        left = num
        result_list = []
        roman_dict = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        while left >= 1:
            max_available = self.getMaxRoman(left, roman_dict)
            result_list.append(roman_dict[max_available])
            left = left - max_available
        return ''.join(result_list)
    
    def getMaxRoman(self, num, roman_dict):
        max_roman = 0
        available_roman = list(roman_dict.keys())
        for index, ava in enumerate(available_roman):
            if available_roman[index] <= num and index < len(available_roman) - 1:
                print("{0} {1} {2}".format(available_roman[index], num, available_roman[index+1]))
                max_roman = available_roman[index] if available_roman[index + 1] > num else max_roman
            elif available_roman[index] <= num and index == len(available_roman) - 1:
                max_roman = available_roman[index]
        return max_roman

if __name__ == '__main__':
    s = sys.argv[1]
    solution = Solution()
    result = solution.intToRoman(s)
    print(result)