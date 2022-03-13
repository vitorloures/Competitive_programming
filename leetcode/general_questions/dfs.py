# Depth First Search Algorithm Implementation (Easy)

# Time Complexity: O(v+e), Where v is the number of
# vertices and e is the number of edges
# But: v = e + 1
# Space Complexity: Worst O(v)

# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        self.depthFirstSearchHelper(self, array)
        return array

    def depthFirstSearchHelper(self, node, array):
        array.append(node.name)
        for child_node in node.children:
            self.depthFirstSearchHelper(child_node, array)