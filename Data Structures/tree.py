"""
Trees

A tree is a nonlinear (or hierarchical) data structure. A tree can be empty with no nodes or a tree is a structure
consisting of one node called the root and zero or one or more subtrees. A tree represent relationships between
different nodes.

If there are two "downward" references pointing to the same node then it is not a tree.

A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can have
only 2 children, we typically name them the left and right child.
"""


class Node:

    """ Binary Tree """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sum_values(root):
    if root is None:
        return 0
    return root.data + sum_values(root.left) + sum_values(root.right)


#  Our example tree looks like this:
#         2
#       /   \
#      3     4
#     / \
#    5   6

node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node2.left = node3
node2.right = node4
node3.left = node5
node3.right = node6

print("Sum of all values of this tree is (should print 20):")
print(sum_values(node2))
