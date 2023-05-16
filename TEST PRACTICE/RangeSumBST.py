class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        return self.helper(root, low, high, 0)

    def helper(self, node, left, right, total):
        if node is None:
            return total

        if low <= node.val <= high:
            total += node.val
            total = self.helper(node.left, left, right, total)
            total = self.helper(node.right, left, right, total)

        if node.val < left:
            total = self.helper(node.right, left, right, total)

        if node.val > right:
            total = self.helper(node.left, left, right, total)

        return total

def print_range_sum(root, low, high):
    # Create the tree from the input list
    tree = TreeNode(root)
    tree.left = TreeNode(5)
    tree.right = TreeNode(15)
    tree.left.left = TreeNode(3)
    tree.left.right = TreeNode(7)
    tree.right.left = None
    tree.right.right = TreeNode(18)

    # Calculate the range sum using the Solution class
    solution = Solution()
    range_sum = solution.rangeSumBST(tree, low, high)

    # Print the range sum
    print(range_sum)

# Create the root of the tree
root = TreeNode(10)

# Call the print_range_sum function with the root of the tree and the low and high values
print_range_sum(root, 7, 15)
