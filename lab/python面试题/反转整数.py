# https://leetcode-cn.com/problems/reverse-integer/submissions/
# 不断出以0，直到商为0，余数存list
# list中拿到余数不断×10的次方
class Solution:
    def reverse(self, x: int) -> int:

        # res = []
        raw_input_int = x
        input_int = abs(raw_input_int)
        res_num = 0

        while 1:
            mode_num = input_int % 10
            input_int = input_int // 10

            res_num = res_num * 10 + mode_num
            if res_num > 2 ** 31 - 1 or res_num < -2 ** 31:
                return 0
            if input_int == 0:
                break
        if raw_input_int<0:
            res_num=-res_num
        return res_num
s=Solution()
rs=s.reverse(-114234)
print(rs)