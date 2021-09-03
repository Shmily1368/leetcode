#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, ans, n = 0, 0, len(nums)
        count = 0

        for r in range(n):
            count += nums[r]

            while count >= target and l <= r:
                if ans == 0: 
                    ans = r - l + 1 
                else: 
                    ans = min(ans, r - l + 1)
                count -= nums[l]
                l += 1
        
        return ans

# @lc code=end

