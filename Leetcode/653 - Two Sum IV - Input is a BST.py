# Definition for a binary tree node.
# (was just a comment in leetcode)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Idea 1:
# for each node in the tree:
#    search the entire tree (except this node) for the complement value
# Time: O(n log n)
# Space: O(1) or O(h) because of recursion stack, where h is the height of the tree
# -- So, if balanced, O(log n), if unbalanced, O(n)
# Could it be better??
#
# Idea 2:
# use a set to store the target values
# Time: O(n)
# Space: O(n) - the set can grow up to O(n) in the worst case
# -- Doesn't take advantage of the fact that the tree is a BST though
# not going to implement it, but it probably works well

class SolutionA:
    def is_val_in_tree(self, root: TreeNode, target: int) -> bool:
        current = root

        while current:
            if target == current.val:
                return True
            elif target < current.val:
                current = current.left
            elif target > current.val:
                current = current.right

        return False

    def recursive_find(self, root: TreeNode, current: TreeNode | None, k: int) -> bool:
        if not current:
            return False
        complement = k - current.val
        return (
            (complement != current.val and self.is_val_in_tree(root, complement))
            or self.recursive_find(root, current.left, k)
            or self.recursive_find(root, current.right, k)
        )

    def findTarget(self, root: TreeNode | None, k: int) -> bool:
        if not root:
            return False
        return self.recursive_find(root, root, k)
