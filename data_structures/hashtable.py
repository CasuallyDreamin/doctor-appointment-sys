from .arr import arr
from .sll import sll

class hashtable:
    def __init__(self):
        self.arr = arr()
        self.size = self.arr.size
        self.occupied = 0
        self.expand_factor = 0.8
    
    def insert(self, key, value):
        
        if self.occupied / self.size >= self.expand_factor:
            self.expand()

        index = self.hash_func(key)
        new_data = key_value(key, value)
        
        #linear probing
        while self.arr.get(index) != None:
            if self.arr.get(index).key == key:
                return False
            index = (index + 1) % self.size

        self.arr.insert(index, new_data)
        self.occupied += 1
        return True
    
    def get(self, key):
        index = self.hash_func(key)
        first_index = index

        while self.arr.get(index) != None:
            if self.arr.get(index).key == key:
                return self.arr.get(index).value
            index = (index + 1) % self.size
            if index == first_index:
                break

        return None

    def hash_func(self, key):
        try:
            key = str(key)
        except:
            return

        key_length = len(key)
        index = 0

        for i in range(key_length):
            index += ord(key[i])
        
        return index**2 % self.size
    
    def expand(self):
        old_arr = arr(self.size)

        for i in range(old_arr.size):
            data = self.arr.get(i)
            old_arr.insert(i, data)

        self.size = self.size * 2
        self.occupied = 0
        self.arr = arr(self.size)

        for i in range(old_arr.size):
            curr_pair = old_arr.get(i)
            if curr_pair != None:
                self.insert(curr_pair.key, curr_pair.value)

    def update(self, key, new_value):
        to_update = self.get_pair(key)
        
        if to_update == None:
            return False
        
        to_update.value = new_value
       
    def get_pair(self, key):
        index = self.hash_func(key)
        first_index = index

        while self.arr.get(index) != None:
            if self.arr.get(index).key == key:
                return self.arr.get(index)
            index = (index + 1) % self.size
            if index == first_index:
                break

        return None
    
    def get_all(self) -> sll:
        all = sll()
        
        for i in range(self.size):
            curr = self.arr.get(i)
            if curr != None:
                all.add_last(curr.value)
                
        
        return all

class key_value:
    def __init__(self, key, value):
        self.key = key
        self.value = value