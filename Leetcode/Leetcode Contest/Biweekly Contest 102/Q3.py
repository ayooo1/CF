# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque([root])
        hmap = {}
        total = 0
        while dq:
            size = len(dq)
            temp = 0
            for i in range(size):
                curr = dq.popleft()
                curr.val = max(0,total - curr.val - (hmap[curr] if curr in hmap else 0))
                if curr.left and curr.right:   
                    hmap[curr.left] = curr.right.val
                    hmap[curr.right] = curr.left.val
                    temp += curr.left.val + curr.right.val
                    dq.append(curr.left)
                    dq.append(curr.right)
                elif curr.right:
                    temp += curr.right.val
                    dq.append(curr.right)
                elif curr.left:
                    temp += curr.left.val
                    dq.append(curr.left)
            total = temp
        return root