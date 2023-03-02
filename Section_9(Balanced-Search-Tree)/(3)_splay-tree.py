# Splay Tree
# ==========
# A Splay tree is a self-adjusting binary search tree invented by Sleator and Tarjan. Unlike an AVL tree (or a Red-Black tree), the structure of the splay tree changes even after the search operation.
# Every time we search an item x or insert x, it moves x to the root of the tree so that the next access of x is quick.
# The goal of the splay tree is not to make every operation fast rather make the sequence of operations fast.
# The individual operation in the splay tree can, sometimes, take O(n) time making the worst case running time linear.
# The sequence of operations, however, take O(logn) amortized time per operation. In other words, the sequence of M operations takes O(Mlogn) time.
# Since the splay tree adjusts itself according to usage, it performs much more efficiently than other binary search trees if the usage pattern is skewed.
# Unlike an AVL or a Red-Black tree where the tree must maintain their invariants all the time, the structure of the splay tree can be in any arbitrary state (although it should maintain the binary search tree invariants all the time)
# but during every operation, it restructures the tree to improve the efficiency of future (incoming) operations.
# The splay tree moves a node x to the root of the tree by performing series of single and double tree rotations.
# Each double rotations moves x to its grandparent’s place and every single rotation moves x to its parent’s place.
# We perform these rotations until x reaches to the root of the tree. This process is called splaying.
# Besides moving x to the root, splaying also shortens the height of the tree which makes the tree more balanced.
#
# There are two types of single rotations and four types of double rotations. Each of them is explained in detail below.
#
# Zig Rotation: Zig is a single rotation. We do zig rotation on node x if x is a left child and x does not have a grandparent (i.e. x’s parent is a root node).
# To make the zig rotation, we rotate x’s parent to the right.
#
# Zag Rotation: Zag rotation is a mirror of zig rotation. We do zag rotation on node x if x is a right child and x does not have a grandparent.
# To make the zag rotation, we perform a left rotation at x’s parent node.
#
# Zig-Zig Rotation: Zig-Zig is a double rotation. We do a zig-zig rotation on x when x is a left child and x’s parent node is also a left child.
# The zig-zig rotation is done by rotating x’s grandparent node to the right followed by right rotation at x’s parent node.
#
# Zag-Zag Rotation: Zag-Zag rotation is a mirror of zig-zig rotation. We do zag-zag rotation on x if x is a right child and x’s parent is also a right child.
# To make the zag-zag rotation, we first do a left rotation at x’s grandparent and then do the left rotation at x’s parent node.
#
# Zig-Zag Rotation: Zig-zag rotation is also a double rotation. We perform zig-zag rotation on x when x is a right child and x’s parent is a left child.
# Zig-zag rotation is done by doing a left rotation at x’s parent node followed by right rotating x grandparent (new parent) node.
#
# Zag-Zig Rotation: The last rotation is the zag-zig rotation. It is a mirror of zig-zag rotation.
# To do zag-zig rotation on node x, we do the right rotation at x’s parent node and left rotation at x grandparent (new parent) node.
#
# Text Source:
# Title: Splay Trees (with implementations in C++, Java, and Python)
# Author: Algorithm Tutor
# URL: https://algorithmtutor.com/Data-Structures/Tree/Splay-Trees/

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
