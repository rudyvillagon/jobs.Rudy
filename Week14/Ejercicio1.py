class Node:


    def __init__(self, data, top_node = None):
        self.data = data
        self.next = top_node


    def __str__(self):
        return str(self.data)
    


class Stack:

    def __init__(self):
        self.top = None


    def is_empty(self):
        return self.top is None


    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top  
        self.top = new_node  
        print(f"\n🔝 The top of the pile is: {new_node}")
        return new_node

    def pop(self):
        if self.is_empty():
            print(" = = The pile is empty = = ")
            return None
        delet_node = self.top
        self.top = self.top.next  
        print(f"\n ❌ You Remove: {delet_node}")
        
    

    def print_stack(self):
        current = self.top
        print("\n 📚 The current Stack is:")
        while current is not None:
            print(f"-----{current.data}")
            current = current.next




stack = Stack()

stack.push("A")
stack.push("B")
stack.push("C")

stack.print_stack()

stack.push("D")

stack.pop()
stack.pop()
stack.pop()

stack.print_stack()