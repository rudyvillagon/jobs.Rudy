class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


    def __str__(self):
        return str(self.data)    
    

class Double_Ended_Queue:


    def __init__(self):
        self.end_left = None
        self.end_right = None


    def is_empty(self):
        return self.end_right is None
    

    def push_left(self, data):
        new_node = Node(data)
        if self.end_right is None:  
            self.end_left = self.end_right = new_node
            print(f"\n ⏮ The left end now is: {new_node}")
        else:
            new_node.next = self.end_left
            self.end_left.prev = new_node
            self.end_left = new_node
            print(f"\n ⏮ The left end now is: {new_node}")
            return new_node
        
    def push_right(self, data):
        new_node = Node(data)
        if self.end_left is None: 
            self.end_left = self.end_right = new_node
            print(f"\n ⏭ The right end now is: {new_node}")
        else:
            new_node.prev = self.end_right
            self.end_right.next = new_node
            self.end_right = new_node  
            print(f"\n ⏭ The right end now is: {new_node}")
            return new_node
        
    def pop_left(self):
        if self.is_empty():
            print(" = = The pile is empty = = ")
            return None
        delet_left = self.end_left 
        self.end_left  = delet_left.prev
        if self.end_left is not None:
            self.end_left.next = None  
        else:
            self.front = None
        print(f"\n ❌ You Remove: {delet_left}")
        
    def pop_right(self):
        if self.is_empty():
            print(" = = The pile is empty = = ")
            return None
        delet_right = self.end_right
        self.end_right  =  delet_right.prev
        if self.end_right is not None:
            self.end_right.next = None  
        else:
            self.front = None
        print(f"\n ❌ You Remove: {delet_right}")
        

    
    def print_stack(self):
        current = self.end_left
        print("\n 📚 The current Stack is:")
        while current is not None:
            print(f"-----{current.data}")
            current = current.next



deq = Double_Ended_Queue()


deq.push_left("A")
deq.push_right("B")
deq.push_left("C")

deq.print_stack()

deq.pop_right()

deq.print_stack()

deq.push_right("D")
deq.push_left("E")

deq.print_stack()