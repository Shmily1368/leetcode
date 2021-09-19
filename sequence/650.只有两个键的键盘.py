#
# @lc app=leetcode.cn id=650 lang=python3
#
# [650] 只有两个键的键盘
#

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        i = 2
        while i*i <= n:
            while n % i == 0:
                n //= i
                ans += i
            i += 1

        if n>1:
            ans += n
        return ans 

# @lc code=end

