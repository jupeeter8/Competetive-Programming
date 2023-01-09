# LC 144
# Given the root of a tree, return the pre order traversal of the tree

# Appraoch 1: Recursive
# Approach 2: Iterative


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:

        return f"TreeNode({self.val}, {self.left}, {self.right})"


class Solution:
    def preorderTraversal(self, root):
        trav = []

        def traverse(root):
            if root == None:
                return None
            trav.append(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return trav


root = TreeNode(
    1, left=(TreeNode(7, right=(TreeNode(12)))), right=(TreeNode(2, left=TreeNode(3)))
)
print(root)
sol = Solution()

print(sol.preorderTraversal(root))
