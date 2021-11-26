#
# @lc app=leetcode.cn id=458 lang=python3
#
# [458] 可怜的小猪
#

# @lc code=start
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log(buckets)/math.log((minutesToTest/minutesToDie)+1))
# @lc code=end

