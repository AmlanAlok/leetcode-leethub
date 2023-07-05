# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return ans2(root)
    
def max_depth(root):
    
    if root is None:
        return 0
    
    return 1 + max(max_depth(root.left), max_depth(root.right))
    
def ans2(root, levels=None, idx = 0):
    if levels is None:
        levels = [None]*max_depth(root)
    if root is None:
        return
    
    if levels[idx] is None:
        levels[idx] = [root.val]
    else:
        levels[idx] += [root.val]
        
    ans2(root.left, levels, idx + 1)
    ans2(root.right, levels, idx + 1)
    return levels

    
def ans1(root):

    if root is None:
        return 
    
    level = []

    ans1(root.left)
    ans1(root.right)
    
    return