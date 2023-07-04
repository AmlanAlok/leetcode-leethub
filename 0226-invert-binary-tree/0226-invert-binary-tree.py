# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return ans2(root)
    
# def ans1(root):
    
#     if root:
        
#         if root.left is None and root.right is None:
#             return root
        
#         if root.left:
#             node = ans1(root.left)
#             temp = root.left
#             root.left = root.right
#             root.right = temp
#         if root.right:
#             node = ans1(root.right)
#             temp = root.left
#             root.left = root.right
#             root.right = temp
#     print(root.val)
#     return root

def ans2(root):
    
    # if not root:
    if root is None:
        return None
    right = ans2(root.right)
    left = ans2(root.left)
    root.left = right
    root.right = left
    
    return root

    
'''
[2,1,3]
[4,2,7,1,3,6,9]
[]
'''