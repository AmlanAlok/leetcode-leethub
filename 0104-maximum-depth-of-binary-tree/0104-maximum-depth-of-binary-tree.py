'''
[3,9,20,null,null,15,7]
[1,null,2]
[]
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return ans2(root)
    
def max_depth(root: TreeNode):
    
    if root.left is None and root.right is None:
        return 1
    
    ans = None
    
    if root.left:
        v = max_depth(root.left) + 1
        if ans is None or ans < v:
            ans = v
    if root.right:
        v = max_depth(root.right) + 1
        if ans is None or ans < v:
            ans = v
    
    return ans
    
    
def ans1(root):
    if root:
        return max_depth(root)
    return 0
    
def ans2(root):
    
    if root == None:
        return 0
    
    return 1 + max(ans2(root.left), ans2(root.right))
        
        
    
    
        