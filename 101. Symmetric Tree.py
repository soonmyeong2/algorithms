class Solution(object):
    def isSymmetric(self, root):
        def mirror(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return p.val == q.val and mirror(p.left, q.right) and mirror(p.right, q.left)
        return mirror(root.left, root.right) if root else True
