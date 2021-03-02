class Solution(object):
    def maxPathSum(self, root):
        self.maxSum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            self.maxSum = max(self.maxSum, node.val + left + right)
            return max(node.val + max(left, right), 0)
        dfs(root)
        return self.maxSum
