class TreeNode:
   def __init__(self, data, left = None, right = None):
      self.val = data
      self.left = left
      self.right = right
class Solution:
   def helper(self, root, h, currentHeight):
      if not root:
         return
         self.helper(root.left, h, currentHeight + 1)
         self.helper(root.right, h, currentHeight + 1)
         if currentHeight < h:
            if currentHeight % 2 == 0:
               if root.left and root.right:
                  root.val = max(root.left.val, root.right.val)
               elif root.left:
                  root.val = root.left.val
               elif root.right:
                  root.val = root.right.val
               else:
                  if root.left and root.right:
                     root.val = min(root.left.val, root.right.val)
                  elif root.left:
                     root.val = root.left.val
                  elif root.right:
                     root.val = root.right.val
   def height(self, root):
      if not root:
         return 0
         return 1 + max(self.height(root.left), self.height(root.right))
   def solve(self, root):
         h = self.height(root)
         self.helper(root, h, 0)
         return root
   def print_tree(root):
      if root is not None:
         print_tree(root.left)
         print(root.val, end = ', ')
      print_tree(root.right)
ob = Solution()
root = TreeNode(0)
root.left = TreeNode(3)
root.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(0)
root.right.left.left = TreeNode(-3)
root.right.right.right = TreeNode(4)
print_tree(ob.solve(root))
