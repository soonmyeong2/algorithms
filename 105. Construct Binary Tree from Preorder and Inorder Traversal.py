class Solution(object):
    # time : 124ms / mem : 52.3mb
    def buildTree(self, preorder, inorder):
        if inorder:
            fork = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[fork])
            root.left = self.buildTree(preorder, inorder[:fork])
            root.right = self.buildTree(preorder, inorder[fork + 1:])
            return root
        
        
    # optimize version 
    # time : 40ms / mem : 18.6mb
    def buildTree2(self, preorder, inorder):
        preorder = collections.deque(preorder)
        inorder_dict = {n: i for i, n in enumerate(inorder)}
		
        def build_tree(start, end):
            if start > end: 
                return None
            root_index = inorder_dict[preorder.popleft()]
            root = TreeNode(inorder[root_index], build_tree(start, root_index - 1), build_tree(root_index + 1, end))
            return root
        return build_tree(0, len(inorder) - 1)
