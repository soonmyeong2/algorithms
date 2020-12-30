class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        
        queue, order = [root], list()
        while queue:
            level = list(queue)
            queue = list()
            order.append([node.val for node in level if node])
            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return order