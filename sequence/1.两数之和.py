#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if i == len(nums)-1:
                return
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
# @lc code=end


