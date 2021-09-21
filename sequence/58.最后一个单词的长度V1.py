#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        while len(s)!=0:
            if s[-1]==" ":
                s = s[:-1]
            else:
                break
        # a = s.split(" ")
        
        # print(a)
        return len(s.split(" ")[-1])
# @lc code=end

