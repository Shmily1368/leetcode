#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        NUM = 1
        if not headA or not headB:
            return null

        A,B = headA,headB
        while A != B:
            if A is None:
                A = headB
            else:
                print(NUM)
                NUM += 1
                A = A.next
            if B is None:
                B = headA
            else:
                B = B.next
        return A
            