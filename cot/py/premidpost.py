import sys

input = sys.stdin.readline

class Node:
    def __init__(self, num, val, left, right):
        self.num = num
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"Node(num={self.num}, val = {self.val}, right={self.right}, left={self.left})"

def main():
    n = int(input())
    tree = [list(input().split()) for _ in range(n)]

    num = 0

    nodes = {}
    for i, j, t in tree:
        nodes[i] = Node(i, num, j, t)
        num += 1

    root = nodes["A"]
    print("".join(pre_trel(root, nodes)))
    print("".join(mid_trel(root, nodes)))
    print("".join(post_trel(root, nodes)))

def pre_trel(node, nodes):
    if node == ".":
        return []
    left_sb = pre_trel(nodes[node.left], nodes) if node.left != "." else []
    right_sb = pre_trel(nodes[node.right], nodes) if node.right != "." else []
    return [node.num] + left_sb + right_sb

def mid_trel(node, nodes):
    if node == ".":
        return []
    left_sb = mid_trel(nodes[node.left], nodes) if node.left != "." else []
    right_sb = mid_trel(nodes[node.right], nodes) if node.right != "." else []
    return left_sb + [node.num] + right_sb

def post_trel(node, nodes):
    if node == ".":
        return []
    left_sb = post_trel(nodes[node.left], nodes) if node.left != "." else []
    right_sb = post_trel(nodes[node.right], nodes) if node.right != "." else []
    return left_sb + right_sb + [node.num]
main()