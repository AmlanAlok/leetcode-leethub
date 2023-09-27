# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return p1(p, q)
    
def ans1(p, q):
    
    if p and q:
        if p.val == q.val:
            if p.left is None and p.right is None:
                if q.left is None and q.right is None:
                    return True

            return ans1(p.left, q.left) and ans1(p.right, q.right)

        return False
    # This if checks None == None and [] == []
    if p == q:
        return True
    return False

'''
[1,2,3]
[1,2,3]
[1,2]
[1,null,2]
[1,2,1]
[1,1,2]
[]
[]
'''

def p1(p, q):
    
    if p and q:
        if p.val == q.val:
            if p1(p.left, q.left) and p1(p.right, q.right):
                return True
            else:
                return False
        return False
    if p == q:
        return True

    return False



















