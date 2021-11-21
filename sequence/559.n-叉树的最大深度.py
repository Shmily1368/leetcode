#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node'):           
        return max((self.maxDepth(children) for children in root.children),default=0)+1 if root else 0
        #if root:
        #    return max((self.maxDepth(children) for children in root.children),default=0)+1
        #return 0
        
# @lc code=end

