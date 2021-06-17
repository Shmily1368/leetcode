#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s):

        nowstr = []
        ans = 0 
        j = 0
        
        while j<len(s):        
            for i in range(j,len(s)):
                if s[i] in nowstr:
                    ans = max(ans,len(nowstr))
                    nowstr = []
                    j = j+1
                    break
                else:
                    nowstr.append(s[i])
        return ans


# @lc code=end
#a = Solution("ohomm")
