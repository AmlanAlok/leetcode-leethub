'''
[5,4,8,11,null,13,4,7,2,null,null,null,1]
22
[1,2,3]
5
[]
0
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return jan3(root, targetSum)
    
def jan3(root, t):
    
    if root is None:
        return False
    
    t -= root.val
    
    if root.left is None and root.right is None:
        return t == 0
    
    l = jan3(root.left, t)
    r = jan3(root.right, t)
    
    return l or r
    '''TC = N, SC = worst N or avg log(n)'''
    
    
    