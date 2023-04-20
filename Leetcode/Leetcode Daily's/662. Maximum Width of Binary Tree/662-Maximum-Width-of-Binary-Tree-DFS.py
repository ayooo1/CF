class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        smallest = {}
        best = 0

        def t(n, d, total):
            if not n:
                return
            
            if d not in smallest:
                smallest[d] = total
            
            nonlocal best
            best = max(best, total - smallest[d] + 1)
            
            t(n.left, d+1, total * 2 + 1)
            t(n.right, d+1, total * 2 + 2)
        

        t(root,0,0)

        return best