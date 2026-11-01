from typing import Optional, TreeNode 

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> list[int]:
        modes = []
        max_count = 0
        count = 0
        prev = None

        def inorder(node):
            nonlocal count, max_count, prev

            if not node:
                return

            inorder(node.left)

            if node.val == prev:
                count += 1
            else:
                count = 1

            if count > max_count:
                max_count = count
                modes.clear()
                modes.append(node.val)
            elif count == max_count:
                modes.append(node.val)

            prev = node.val

            inorder(node.right)

        inorder(root)
        return modes