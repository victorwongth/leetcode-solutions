class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        else:
            return self.sumPath(root, 0, targetSum)

    def sumPath(self, node: TreeNode, sum: int, targetSum: int) -> int:
        sum += node.val
        print(sum)
        if node.left == None and node.right == None:
            if sum == targetSum:
                return True
            else:
                return False 
        elif node.left != None and node.right == None:
            return self.sumPath(node.left, sum, targetSum)
        elif node.right != None and node.left == None:
            return self.sumPath(node.right, sum, targetSum)
        else:
            return (self.sumPath(node.left, sum, targetSum) or self.sumPath(node.right, sum, targetSum))
