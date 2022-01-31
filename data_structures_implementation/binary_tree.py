# TODO: Create algorithm to add a node to a Binary Search Tree

class BinaryNode:
    def __init__(self, nodeval):
        self.node_val = nodeval
        self.left = None
        self.right = None


class BinaryTree:
    root: BinaryNode

    def __init__(self, rootval=0):
        self.root = BinaryNode(rootval)

    def create_example(self):
        self.root.node_val = 10
        self.root.left = BinaryNode(5)
        self.root.right = BinaryNode(20)
        self.root.right.left = BinaryNode(15)
        self.root.left.left = BinaryNode(3)
        self.root.left.right = BinaryNode(7)


bt = BinaryTree()
bt.create_example()


def print_in_order(node: BinaryNode):
    if node.left is not None:
        print_in_order(node.left)
    print(node.node_val, end=" ")
    if node.right is not None:
        print_in_order(node.right)


def print_pre_order(node: BinaryNode):
    print(node.node_val, end=" ")
    if node.left is not None:
        print_pre_order(node.left)
    if node.right is not None:
        print_pre_order(node.right)


def print_post_order(node: BinaryNode):
    if node.left is not None:
        print_post_order(node.left)
    if node.right is not None:
        print_post_order(node.right)
    print(node.node_val, end=" ")


print("\nIn-order transversal")
print_in_order(bt.root)
print("\nPre-order transversal")
print_pre_order(bt.root)
print("\nPost-order transversal")
print_post_order(bt.root)
