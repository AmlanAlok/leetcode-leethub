'''
[3,4,5,1,2]
[4,1,2]
[3,4,5,1,2,null,null,null,null,0]
[4,1,2]
[1,1]
[1]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return ans1(root, subRoot)
    
def e1(root, subRoot):
    
    if root and subRoot:
        if root.val == subRoot.val:
            if ans1(root.left, subRoot.left) and ans1(root.right, subRoot.right):
                return True
        else:
            return ans1(root.left, subRoot) or ans1(root.right, subRoot)
    if root or subRoot:
        return ans1(root.left, subRoot) or ans1(root.right, subRoot)
    if root == subRoot:
        return True
    return False

def ans1(root, subRoot):
    
    def dfs(node):
        
        if node is None:
            return False
        elif is_identical(node, subRoot):
            return True
        return dfs(node.left) or dfs(node.right)
    
    def is_identical(node1, node2):
        
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        
        return (node1.val == node2.val and 
               is_identical(node1.left, node2.left) and
               is_identical(node1.right, node2.right))
    
    return dfs(root)

        
        
        
        
        
        
        
        
    