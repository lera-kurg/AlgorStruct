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

    def find_razvilki(self):
        return self.razvilki_node(self.root)

    def razvilki_node(self, node):
        # обход по LNR (слева направо)
        if node is None:
            return []
        
        result = self.razvilki_node(node.left)

        if node.left is not None and node.right is not None:
            result.append(node.data)

        result += self.razvilki_node(node.right)
        
        return result


n = list(map(int, input().split()))
p = BinaryTree()

for i in n[:-1]:
    p.insert(i)
k = p.find_razvilki()
for i in k:
    print(i)

