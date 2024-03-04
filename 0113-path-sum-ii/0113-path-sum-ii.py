'''
[5,4,8,11,null,13,4,7,2,null,null,5,1]
22
[1,2,3]
5
[1,2]
0
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return sol(root, targetSum)


def is_leaf(node):
	return node.left == None and node.right == None


def sol(root, targetSum):

	if root is None:
		return []

	temp = []
	targetSum -= root.val

	if targetSum == 0 and is_leaf(root):
		return [[root.val]]

	p = [sol(root.left, targetSum), sol(root.right, targetSum)]

	for arr in p:
		for x in arr:
			x.insert(0, root.val)
			temp.append(x)

	return temp