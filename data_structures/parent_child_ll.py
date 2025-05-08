from .sll import sll, sll_node

class parent_child_ll:
    def __init__(self):
        self.head: parent_node = None
        self.tail: parent_node = None

    def add_parent(self, parent_data):
        new_parent = parent_node(parent_data)
        curr_parent = self.head

        if curr_parent == None:
            self.head = new_parent
            self.tail = new_parent
            return True
        
        # check if parent already exists
        while curr_parent != None:
            if curr_parent.data == parent_data:
                return False
            curr_parent = curr_parent.next
        
        new_parent.next = self.head
        self.head = new_parent
        return True
    
    def add_child(self, parent_data, child_data):
        curr_parent = self.head
        # find parent
        while curr_parent != None:
            if curr_parent.data == parent_data:
                curr_parent.children.add_first(child_data)
                return True
            curr_parent = curr_parent.next
        # parent doesn't exist
        return False
    
    def get_children(self, parent_data) -> sll:
        curr_parent = self.head
        # find parent
        while curr_parent != None:
            if curr_parent.data == parent_data:
                return curr_parent.children
            curr_parent = curr_parent.next
        empty_sll = sll()
        
        return empty_sll 
    
    def get_parents(self):
        parents = sll()
        curr_parent = self.head
        
        while curr_parent != None:
            parents.add_first(curr_parent.data)    
            curr_parent = curr_parent.next
                
            
class parent_node(sll_node):
    def __init__(self, data):
        super().__init__(data)
        self.children = sll()