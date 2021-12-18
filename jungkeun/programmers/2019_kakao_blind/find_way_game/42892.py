import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        
def makeTree(nodeinfo) :
    if len(nodeinfo) == 0 :
        return None
    node = max(nodeinfo, key=lambda node : node[2])
    i = nodeinfo.index(node)
    v,x,y = node
    right = makeTree(nodeinfo[i+1:])
    left = makeTree(nodeinfo[:i])
    return Node(v,left,right)

def preorder(tree) :
    if tree is None :
        return []
    return [tree.value] + preorder(tree.left) + preorder(tree.right)

def postorder(tree) :
    if tree is None :
        return []
    return postorder(tree.left) + postorder(tree.right) + [tree.value]

def solution(nodeinfo):
    nodeinfo = [ ( i+1, x, y ) for i, (x, y) in enumerate(nodeinfo)]
    nodeinfo = sorted(nodeinfo, key=lambda node : node[1])
    tree = makeTree(nodeinfo)
    answer = [preorder(tree),postorder(tree)]
    return answer
