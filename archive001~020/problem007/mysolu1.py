class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0

        x_list = list(str(x))
        if x_list[0] == '-':
            x_list[0] = ''
            x_list.append('-')
            x_list.reverse()
            r_x = ''.join(x_list)
            res = int(r_x)
        else:
            x_list.reverse()
            r_x = ''.join(x_list)
            res = int(r_x)
            
        if res < -(2**31) or res > 2**31-1:
            return 0
        else:
            return res