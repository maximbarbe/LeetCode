# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return None
        else:
            max_idx = 0
            max_val = -inf
            for i in range(len(nums)):
                if nums[i] > max_val:
                    max_idx = i
                    max_val = nums[i]
            node = ListNode(max_val)
            node.left = self.constructMaximumBinaryTree(nums[:max_idx])
            node.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
            return node