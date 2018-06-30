#我的版本
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
        
#执行最快版本
class Solution2:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        
        return check(root) != -1
