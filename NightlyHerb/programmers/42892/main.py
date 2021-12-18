"""
https://programmers.co.kr/learn/courses/30/lessons/42892
"""

import sys

sys.setrecursionlimit(100000)


class Tree:
    def __init__(self, node, left, right):
        self.node = node
        self.left = left
        self.right = right

    def __repr__(self):
        """
        >>> repr(Tree(1, Tree(2, None, None), Tree(3, None, None)))
        'Tree(1, Tree(2, None, None), Tree(3, None, None))'
        """
        return f"Tree({repr(self.node)}, {repr(self.left)}, {repr(self.right)})"


def make_tree(index_and_node_list):
    """
    >>> repr(make_tree([]))
    'None'
    >>> repr(make_tree(list(enumerate([[5,3]], 1))))
    'Tree((1, [5, 3]), None, None)'
    >>> repr(make_tree(list(enumerate([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]], 1))))
    'Tree((7, [8, 6]), Tree((4, [3, 5]), Tree((6, [1, 3]), None, Tree((9, [2, 2]), None, None)), Tree((1, [5, 3]), None, Tree((8, [7, 2]), Tree((5, [6, 1]), None, None), None))), Tree((2, [11, 5]), None, Tree((3, [13, 3]), None, None)))'
    """

    if len(index_and_node_list) == 0:
        return None

    if len(index_and_node_list) == 1:
        [index_and_node] = index_and_node_list
        return Tree(index_and_node, None, None)

    def node_height(index_and_node):
        index, (x, y) = index_and_node
        return y

    root_node = max(index_and_node_list, key=node_height)
    _, (root_x, _) = root_node

    left_part, right_part = [], []
    for index_and_node in index_and_node_list:
        _, (x, _) = index_and_node
        if x == root_x:
            continue  # skip root node
        elif x < root_x:
            left_part.append(index_and_node)
        else:
            right_part.append(index_and_node)
    left_tree = make_tree(left_part)
    right_tree = make_tree(right_part)
    return Tree(root_node, left_tree, right_tree)


def preorder_traverse_node_tree(tree, visited):
    if tree is None:
        return
    i, (x, y) = tree.node
    visited.append(i)
    preorder_traverse_node_tree(tree.left, visited)
    preorder_traverse_node_tree(tree.right, visited)


def postorder_traverse_node_tree(tree, visited):
    if tree is None:
        return
    postorder_traverse_node_tree(tree.left, visited)
    postorder_traverse_node_tree(tree.right, visited)
    i, (x, y) = tree.node
    visited.append(i)


def solution(nodeinfo):
    """
    >>> solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])
    [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]
    """
    index_and_node_list = list(enumerate(nodeinfo, 1))
    tree = make_tree(index_and_node_list)
    preorder, postorder = [], []
    preorder_traverse_node_tree(tree, preorder)
    postorder_traverse_node_tree(tree, postorder)
    return [preorder, postorder]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
