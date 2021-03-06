#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        L = len(s)-1
        ans = 0
        while L>=0:
            if s[L] == " ":
                L-=1
            else:
                break
        while L>=0 and s[L]!=" ":
            ans+=1
            L-=1
        return ans

        
# @lc code=end

