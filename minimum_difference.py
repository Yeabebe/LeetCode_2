from typing import Optional, TreeNode      

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        result = float('inf')

        def inorder(node):
            nonlocal prev, result

            if not node:
                return

            inorder(node.left)

            if prev is not None:
                result = min(result, node.val - prev)

            prev = node.val

            inorder(node.right)

        inorder(root)
        return result