class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_Tree:

    def __init__(self):
        self.root = None


    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)
    

    def _insert_recursive(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(data, current_node.left) 
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(data,current_node.right) 
        else:
            print(f"\n ⚠ Repeated data: {data}")
    

    def inorder(self):
        self._inorder_recursive(self.root)


    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.data)
            self._inorder_recursive(node.right)



Bi_tree = Binary_Tree()

Bi_tree.insert(3)
Bi_tree.insert(7)
Bi_tree.insert(4)
Bi_tree.insert(10)
Bi_tree.insert(2)
Bi_tree.insert(6)
Bi_tree.insert(12)

print("\n ✳ traversal in order:")
Bi_tree.inorder()
print("\n")