#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        # print(bin(n))
        # print(str(bin(n)).replace("0b","").replace("0",""))
        return len(str(bin(n)).replace("0b","").replace("0",""))
        # a = str(n).replace("0","")
        # print(a)
        # return len(a)
# @lc code=end

