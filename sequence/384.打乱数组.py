#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#

# @lc code=start
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.origin = nums.copy()

    def reset(self) -> List[int]:
        #self.nums = self.origin.copy()
        #return self.nums
        return self.origin

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            j = random.randrange(i,len(self.nums))
            #self.nums[i] = self.origin
            self.nums[i],self.nums[j] = self.nums[j],self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

