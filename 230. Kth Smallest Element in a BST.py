class Solution:
    def traverse(self, node):
        if node:
            yield from self.traverse(node.left)
            yield node
            yield from self.traverse(node.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        for i, node in enumerate(self.traverse(root)):
            if i == k - 1:
                return node.val
