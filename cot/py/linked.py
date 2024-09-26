def sol(nodelist):
    class Node:
        def __init__(self, num, x, y):
            self.num = num
            self.x = x
            self.y = y
            self.right = None
            self.left = None
        
        def __repr__(self):
            return f"Node(num={self.num}, x={self.x}, y={self.y}, right={self.right}, left={self.left})"
    
    # Node 객체 생성
    nodes = [Node(i + 1, x, y) for i, (x, y) in enumerate(nodelist)]
    
    # y 값이 가장 큰 노드를 루트로 설정
    root = max(nodes, key=lambda node: node.y)
    
    # x 값 기준으로 정렬
    nodes.sort(key=lambda node: node.x)
    
    # 노드를 트리에 삽입하는 함수
    def node_input(node, root):
        if node.x < root.x:
            if root.left:
                node_input(node, root.left)
            else:
                root.left = node
        else:
            if root.right:
                node_input(node, root.right)
            else:
                root.right = node

    # 트리 구성
    for node in nodes:
        if node is not root:
            node_input(node, root)

    # 전위 순회 (root - left - right)
    def preorder(node):
        return [node.num] + preorder(node.left) + preorder(node.right) if node else []
    
    # 전위 순회를 사용하여 결과를 반환
    print(preorder(root))
    return 1

















nodelist = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(sol(nodelist))
    