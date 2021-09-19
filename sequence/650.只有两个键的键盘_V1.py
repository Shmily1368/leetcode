#
# @lc app=leetcode.cn id=650 lang=python3
#
# [650] 只有两个键的键盘
#

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        f = [0]*(n+1)
        for i in range(2,n+1):
            f[i] = float("inf")
            j = 1
            while j*j <= n:
                if i%j == 0:
                    f[i] = min(f[i],f[j]+(i//j))
                    f[i] = min(f[i],f[i//j]+j)
                j+=1
        return f[n]

# @lc code=end

