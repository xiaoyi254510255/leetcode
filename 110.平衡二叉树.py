class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if (abs(self.cal_dep(root.left) - self.cal_dep(root.right))) > 1:
            return False
        else:
            return (self.isBalanced(root.left) and self.isBalanced(root.right))
        
    def cal_dep(self, nod):
        if not nod:
            return 0
        left = self.cal_dep(nod.left)
        right = self.cal_dep(nod.right)
            
        return max(left,right) + 1
        
