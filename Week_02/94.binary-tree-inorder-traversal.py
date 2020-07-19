""" class TreeNode:
    def __init__(self, value: int):
        self.val = value
        self.left, self.right = None, None
def inorder(self, root):
    if root.left is not None:
        inorder(root.left)
    print(root.value)
    if root.right is not None:
        inorder(root.right) """
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # 前序递归
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        #  中序递归 
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        # # 后序递归
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

