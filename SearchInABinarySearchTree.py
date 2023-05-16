class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val= val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        if root == None or root.val == val:
            return root
        
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
        
    def printSubtree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: None
        """
        node = self.searchBST(root, val)
        if node:
            self.printTree(node)

    def printTree(self, node):
        """
        :type node: TreeNode
        :rtype: None
        """
        if not node:
            return
        self.printTree(node.left)
        print(node.val)
        self.printTree(node.right)
    

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

s = Solution()
s.printSubtree(root, 2)  # Output: 1 2 3
