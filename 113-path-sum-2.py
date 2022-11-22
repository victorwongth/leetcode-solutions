import copy

class Solution:
    def __init__(self):
        self.result: List[List[int]] = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return self.result 
        else:
            path = []
            self.sumPath(root, 0, targetSum, path)
            return self.result


    def sumPath(self, node: TreeNode, sum: int, targetSum: int, path: List[int]):
        sum += node.val
        path.append(node.val)
        if node.left == None and node.right == None:
            if sum == targetSum:
                self.result.append(copy.deepcopy(path)) 
        if node.left != None:
            self.sumPath(node.left, sum, targetSum, path)
        if node.right != None:
            self.sumPath(node.right, sum, targetSum, path)
        path.pop()
