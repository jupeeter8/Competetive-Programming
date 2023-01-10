class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:

        return f"TreeNode({self.val}, {self.left}, {self.right})"
