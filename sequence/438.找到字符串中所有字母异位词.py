#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(s) < len(p):
            return []
        
        ans = []
        count  = [0]*26
        for i in range(len(p)):
            count[ord(s[i]) - 97] += 1
            count[ord(p[i]) - 97] -= 1
        differ = [c!=0 for c in count].count(True)
        print(differ)
        if (differ == 0):
            ans.append(0)
        for i in range(len(s)-len(p)):
            if count[ord(s[i]) - 97] == 1:
                differ -= 1
            elif count[ord(s[i]) - 97] == 0 :
                differ += 1
            count[ord(s[i]) - 97] -= 1

            if count[ord(s[i + len(p)]) - 97] == -1:# diff to same
                differ -= 1
            if count[ord(s[i + len(p)]) - 97] == 0: # same to different
                differ += 1
            count[ord(s[i+len(p)]) - 97] += 1
            
            if (differ == 0):
                ans.append(i+1)
        return ans

            
            

# @lc code=end

