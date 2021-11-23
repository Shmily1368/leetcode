#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        #len(s)
        # len = min(len(s),len(goal))
        if len(s) != len(goal):
            return False
        if s == goal:
            if len(set(s)) < len(goal):
                return True
            else:
                return False
        diff = [(a,b) for a,b in zip(s,goal) if a!=b]
        #print(diff)
        #print(len(diff))
        if len(diff) == 2 and diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]:
            return True
        return False

# @lc code=end

