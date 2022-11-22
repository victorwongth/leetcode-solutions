# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def _findPath(value: int, node: TreeNode, path: List[str]) -> bool:
            if node.val == value:
                return True
            if node.left != None:
                if _findPath(value, node.left, path):
                    path.append("L")
                    return True
            if node.right != None:
                if _findPath(value, node.right, path):
                    path.append("R")
                    return True
            if node.left == None and node.right == None:
                return False
            
        start_path: List[str] = []
        dest_path: List[str] = []
        _findPath(startValue, root, start_path)
        _findPath(destValue, root, dest_path)

        while len(start_path) > 0 and len(dest_path) > 0 and start_path[-1] == dest_path[-1]:
            start_path.pop()
            dest_path.pop()

        result: str = ""
        for _ in range(len(start_path)):
            result += "U"
        for ele in reversed(dest_path):
            result += str(ele)

        return result
