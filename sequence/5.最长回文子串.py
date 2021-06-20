#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
import numpy as np
class Solution2:
    # 线性规划，部分case会超时
    def longestPalindrome(self, s: str) -> str:
        result = ""
        a= np.zeros((len(s), len(s)), dtype=np.int)
        # print(a[0][1])
        for i in range(len(s)):
            a[i][i] = 1
        if len(s) == 1 :
            return s
        # if len(s) == 2 :
        #     if s[0] == s[1]:
        #         return s
        #     else:
        #         return s[0]
        leaf = right = len(s)-1
        while(leaf>0):
            leaf -= 1
            right = leaf+1
            if result == "":
                result = s[leaf]
            while(right<len(s)):
                # if a[leaf][right] == 1:
                #     continue                                
                if s[leaf] == s[right] and right - leaf == 1:
                    a[leaf][right] = 1
                    if len(result)<= (right-leaf+1):
                        # print("a",result,s[leaf:right+1])
                        result = s[leaf:right+1]
                        # print("result",result)

                elif(a[leaf+1][right-1] == 1 and s[leaf] == s[right]):
                    a[leaf][right] = 1
                    if len(result)<= (right-leaf+1):
                        # print("b",result,s[leaf:right+1],leaf,right)
                        result = s[leaf:right+1]
                        # print("result",result)
                # print("haha",s[leaf:right])
                # print(a[leaf][right])
        
                right += 1 

        # print(i,j)
        # while(i<=j)
            
        
        return result
class Solution:
    # 线性规划，部分case会超时
    def longestPalindrome(self, s: str) -> str:
        result = ""
        a= np.zeros((len(s), len(s)), dtype=np.int)
        for i in range(len(s)):
            high = i
            low = i
            while(high<len(s)-1 and s[i] == s[high+1]):
                high += 1
            i = high
            while(low-1 >=0 and high+1<len(s) and s[low-1] == s[high+1]):
                high += 1
                low -= 1
            if high - low + 1 > len(result):
                result = s[low:high+1]
        return result

# @lc code=end
test = Solution()
zzz ="zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
re = test.longestPalindrome(zzz)
print(re)
