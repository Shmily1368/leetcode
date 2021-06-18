#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        resultlist = []
        test1 = 0
        test2 = 0
        while(test1 < len(nums1) and test2 < len(nums2)):
            if(nums1[test1] < nums2[test2]):
                resultlist.append(nums1[test1])
                test1 += 1
            else:
                resultlist.append(nums2[test2])
                test2 += 1   
        if(test1< len(nums1)):
            resultlist += nums1[test1:]
        else:
            resultlist += nums2[test2:]
        print(resultlist)

        if(len(resultlist)%2 != 0):
            return resultlist[int(int(len(resultlist)+1)/2)-1]
        else:
            a = resultlist[int(int(len(resultlist))/2)-1]
            b = resultlist[int(int(len(resultlist)+1)/2)]
            return (a+b)/2

        #Time Limit Exceeded
        # while(test1 < len(nums1) or test2 < len(nums2)):
        #     if(test1 < len(nums1) and test2 < len(nums2)):
        #         if(nums1[test1] < nums2[test2]):
        #             resultlist.append(nums1[test1])
        #             test1 += 1
        #         else:
        #             resultlist.append(nums2[test2])
        #             test2 += 1 
        #     elif(test1 < len(nums1)):
        #         resultlist += nums1[test1:]
        #     else:
        #         resultlist += nums2[test2:]
        # print(resultlist)
        # if(len(resultlist)%2 != 0):
        #     return resultlist[len(resultlist)/2]
        # else:
        #     tem = (resultlist[int(len(resultlist)+1)/2]+resultlist[int(len(resultlist)-1)/2])/2
        #     return tem
        
# @lc code=end
