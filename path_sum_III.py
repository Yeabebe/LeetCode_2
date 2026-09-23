from typing import TreeNode    

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        prefix = {0: 1}

        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum += node.val

            # Need an earlier prefix sum of current_sum - targetSum
            count = prefix.get(current_sum - targetSum, 0)

            prefix[current_sum] = prefix.get(current_sum, 0) + 1

            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            # Remove this prefix sum when going back up
            prefix[current_sum] -= 1

            return count

        return dfs(root, 0)