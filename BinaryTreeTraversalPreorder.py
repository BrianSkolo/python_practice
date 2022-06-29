# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# preOrder = (root, left, right)
# stack = [1] first we add the root to our stack
# result = [ 1] then append it to our result list
# then empty the stack [] and so on...
class Solution:
    def preOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        while root or stack:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop() 
            root = root.right
        return result
            