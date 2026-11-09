class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        node = self.root
        while True:
            if key < node.data:
                if node.left is None:
                    node.left = Node(key)
                    return
                node = node.left
            elif key > node.data:
                if node.right is None:
                    node.right = Node(key)
                    return 
                node = node.right
            else:
                return
            
    def find_listok(self):
        return self.listok_node(self.root)

    def listok_node(self, node):
        if node is None:
            return []
        if node.left is None and node.right is None:
            return [node.data]
        return self.listok_node(node.left) + self.listok_node(node.right)
    

n = list(map(int, input().split()))    
p = BinaryTree()

for i in n[:-1]:
    p.insert(i)

k = p.find_listok()
for i in k:
    print(i)