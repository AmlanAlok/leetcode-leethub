# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return ans(root)
    
def ans(root):
    st_nums = helper(root)
    total = 0
    for n in st_nums:
        total += int(n)
    return total

def helper(node):
    
    if node is None:
        return []
    
    all_paths = []
    
    if node.left is None and node.right is None:
        return [str(node.val)]
    
    temp = [helper(node.left), helper(node.right)]
    
    for child in temp:
        for st in child:
            st = str(node.val) + st
            all_paths.append(st)
    
    return all_paths