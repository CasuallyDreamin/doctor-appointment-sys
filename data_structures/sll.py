class sll:
    def __init__(self):
        self.head: sll_node = None
        self.tail: sll_node = None

    def add_first(self, data):
        new_node = sll_node(data)
        
        new_node.next = self.head
        self.head = new_node
        
        if self.tail == None:
            self.tail = new_node

    def add_last(self, data):
        new_node = sll_node(data)

        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node

    

class sll_node:
    def __init__(self, data):
        self.data = data
        self.next: sll_node = None