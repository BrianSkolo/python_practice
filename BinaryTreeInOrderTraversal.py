# Definition for a binary tree node.
class TreeNode:
    # accepts a value for root(val), left child (left), and right child (right)
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # the function called inOrderTraversal accepts the arguments self (instance/ item), and root with a value called TreeNode, and )
    def inOrderTraversal(self, root: [TreeNode])
    # we want the output to be stored in a list called result
        result = []
        # if there is no root return none.  if not take the left child and add it to the end of the list (result), add the root value to the list (result), and take the right child and add it to the end of the list
        if root != None:
            result.extend(self.inorderTraversal(root.left))
            result.append(root.val)
            result.extend(self.inorderTraversal(root.right))