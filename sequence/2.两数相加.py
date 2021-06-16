#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        re = ListNode(0)
        r = re
        s = 0
        while(l1 or l2):
            
            if l1:
                x = l1.val 
            else:
                x = 0
            if l1!= None:
                l1 = l1.next
            
            if l2:
                y = l2.val
            else:
                y = 0
            if l2!=None:
                l2 = l2.next
            tem = x+y+s
            s = tem//10
            r.next = ListNode(tem%10)
            r = r.next
        if s>0:
            r.next = ListNode(1)
        return re.next



        
        

# @lc code=end

