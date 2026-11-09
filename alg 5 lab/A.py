from sys import stdin

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def ADD(self, n):
        if not self._search(self.root, n):
            self.root = self._ADD(self.root, n)
            return True
        else:
            return False

    def _ADD(self, node, n):
        if node is None:
            return Node(n)
        if n < node.data:
            node.left = self._ADD(node.left, n)
        elif n > node.data:
            node.right = self._ADD(node.right, n)
        return node

    def search(self, x):
        return self._search(self.root, x)

    def _search(self, node, x):
        if node is None:
            return False
        if node.data == x:
            return True
        if x < node.data:
            return self._search(node.left, x)
        return self._search(node.right, x)

    def _max_node(self, node):
        c = node
        while c.right is not None:
            c = c.right
        return c

    def delete(self, key):
        if self._search(self.root, key):
            self.root = self._delete(self.root, key)
            return True
        else:
            return False
        

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.data:
            node.left = self._delete(node.left, key)
        elif key > node.data:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            max_node = self._max_node(node.left)
            node.data = max_node.data
            node.left = self._delete(node.left, max_node.data)
        return node  

    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, node, level):
        if node == None:
            return
        
        self._print_tree(node.left, level+1)

        print('.' * level + str(node.data))
        self._print_tree(node.right, level+1)


tree = BinarySearchTree()
for line in stdin:
    c = line.split()
    # print(c)

    if not c:
        continue

    if c[0] == 'ADD':
        if tree.ADD(int(c[1])):
            print("DONE")
        else:
            print("ALREADY")

    if c[0] == "SEARCH":
        if tree.search(int(c[1])):
            print("YES")
        else:
            print("NO")

    if c[0] == "DELETE":
        if tree.delete(int(c[1])):
            print("DONE")
        else:
            print("CANNOT")

    if c[0] == "PRINTTREE":
        tree.print_tree()

    