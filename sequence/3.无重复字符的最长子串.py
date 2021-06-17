#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start

# test 1
# class Solution:
#     def lengthOfLongestSubstring(self, s):

#         nowstr = []
#         ans = 0 
#         j = 0
        
#         while j<len(s):        
#             for i in range(j,len(s)):
#                 if s[i] in nowstr:
#                     ans = max(ans,len(nowstr))
#                     nowstr = []
#                     j = j+1
#                     break
#                 else:
#                     nowstr.append(s[i])
#         return ans
#----------------------------
# test 2
# class Solution:
#     def lengthOfLongestSubstring(self, s):

#         nowstr = []
#         ans = 0 
#         j = 0
        
#         while j<len(s):        
#             for i in range(j,len(s)):
#                 if s[i] in nowstr:
#                     ans = max(ans,len(nowstr))
#                     nowstr = []
#                     j = j+1
#                     break
#                 else:
#                     nowstr.append(s[i])
#         return ans
#---------------
# test 3
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        # i是记录某个字符串最近一次出现的位置（非这次）
        # st list来记录当前最新出现位置
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans
# @lc code=end
#a = Solution("ohomm")
