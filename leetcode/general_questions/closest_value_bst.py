# Find Closest Value in BST (Easy)

# Time Complexity: Average case O(log(N)), Worst case O(N),
# where N is the number of node in the BST
# Space Complexity: O(1)

def findClosestValueInBst(tree, target):
    closest_value = tree.value
    min_diff = abs(target - tree.value)
    while tree:
        cur_diff = abs(target - tree.value)
        if cur_diff < min_diff:
            min_diff = cur_diff
            closest_value = tree.value
        if target > tree.value:
            tree = tree.right
        elif target < tree.value:
            tree = tree.left
        else:
            return tree.value

    return closest_value


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
