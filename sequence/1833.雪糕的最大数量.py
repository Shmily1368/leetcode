#
# @lc app=leetcode.cn id=1833 lang=python3
#
# [1833] 雪糕的最大数量
#

# @lc code=start
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        result = 0
        costs.sort()
        for tem in costs:
            if tem<=coins:
                result += 1
                coins -= tem
        return result
# @lc code=end

