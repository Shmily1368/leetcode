#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
import numpy as np
import math
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<=1:
            return s
        if len(s)<3:
            return s
        if len(s) == 3:
            if numRows == 2:
                return s[0]+s[2]+s[1]
            else:
                return s
        strnum = 0
        singleline = numRows - 2
        linenum = math.ceil(len(s)/(2*numRows-2)*(numRows-1))
        resultlist = np.zeros((numRows,linenum),dtype=np.str)
        #print(resultlist[0][6])
        i = 0
        flag = True
        while i<linenum and flag == True:
            for j in range(numRows):
                print(j,i)
                resultlist[j][i] = s[strnum]
                strnum += 1
                if strnum == len(s):
                    flag = False
                    break
            for j in range(singleline):
                print("j","-:",j)
                if i+1 == linenum:
                    break
                if strnum == len(s):
                    flag = False
                    break
                resultlist[numRows-1-j-1][i+1] = s[strnum]
                strnum += 1
                if strnum == len(s):
                    flag = False
                    break
                i += 1
            print(resultlist)
            i += 1
        
        #print(resultlist)
        res = ""
        for one in resultlist:
            for j in one:
                if j!="":
                    res += j
        return res

# @lc code=end

