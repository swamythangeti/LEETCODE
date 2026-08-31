class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float('-inf')
        def dfs(node):
            nonlocal maxi
            if node is None:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            maxi = max(maxi, left + right + node.val)
            return node.val + max(left, right)
        dfs(root)
        return maxi