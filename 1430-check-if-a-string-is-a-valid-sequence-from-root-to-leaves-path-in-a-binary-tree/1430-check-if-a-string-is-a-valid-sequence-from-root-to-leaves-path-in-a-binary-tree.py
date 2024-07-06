# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        return ans(root, arr, 0)
    
def ans(node, arr, idx):
    '''TC=n, SC=n or log(n) same as 112'''
    if node is None or idx == len(arr):
        return False
    
    if arr[idx] != node.val:
        return False
    
    if not (node.left or node.right) and idx == len(arr)-1:
        return True
    
    return ans(node.left, arr, idx+1) or ans(node.right, arr, idx+1)

'''
[0,1,0,0,1,0,null,null,1,0,0]
[0,1,0,1]
[0,1,0,0,1,0,null,null,1,0,0]
[0,0,1]
[0,1,0,0,1,0,null,null,1,0,0]
[0,1,1]
'''