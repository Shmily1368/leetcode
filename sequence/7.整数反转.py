#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        n=0
        while x != 0:
            if n < INT_MIN //10 + 1 or n > INT_MAX//10:
                return 0
            yu = x%10
            if x < 0 and yu >0:
                yu -= 10
            x = (x - yu)//10
            n = n*10 + yu
        return  n
        # while x!=0:
        #     n = n*10 + x%10
        #     x = int(x/10)
        # return n if int(n) == n else 0
# @lc code=end

