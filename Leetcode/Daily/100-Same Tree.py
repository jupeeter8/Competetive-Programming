from typing import Optional
from CreateDataStructures.mytrees import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        isSame = [True]

        def eqTree(p, q):
            if p is None and q is None:
                return None
            if p is None or q is None:
                isSame[0] = False
                return None
            isSame[0] = isSame[0] & (p.val == q.val)
            eqTree(p.left, q.left)
            eqTree(p.right, q.right)

        eqTree(p, q)

        return isSame[0]


def main():
    p = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    q = TreeNode(1, left=TreeNode(2), right=TreeNode(3))

    sol = Solution()

    print(sol.isSameTree(p, q))


main()
