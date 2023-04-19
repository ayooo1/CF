# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q=collections.deque([(root,'r',0), (root,'l',0)])
        m = 0

        while q:
            cur,d,l = q.popleft()
            m = max(m,l)
            if d == 'r':
                if cur.left:
                    q.append((cur.left,'l',l+1))
                if cur.right:
                    q.append((cur.right,'r',1))
            
            if d == 'l':
                if cur.right:
                    q.append((cur.right,'r',l+1))
                if cur.left:
                    q.append((cur.left,'l',1))
        
        return m