# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root,1)])
        width = 0
        while q:
            _,left = q[0]
            _,right = q[-1]
            width = max(width, right - left+1)
            next_level = deque()
            
            while q:
                node, index = q.popleft()
                if node.left: next_level.append((node.left, index*2))
                if node.right: next_level.append((node.right, index*2+1))
            q = next_level
        return width
            
        