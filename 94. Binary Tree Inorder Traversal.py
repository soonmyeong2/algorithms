#recursive
class Solution(object):
    def inorderTraversal(self, root):
        ans = list()

        def inorder(root):
            if root:
                inorder(root.left)
                ans.append(root.val)
                inorder(root.right)

        inorder(root)
        return ans


#iterative
class Solution(object):
    def inorderTraversal(self, root):
        ans = list()
        stack = list()

        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                return ans

            node = stack.pop()
            ans.append(node.val)
            root = node.right
