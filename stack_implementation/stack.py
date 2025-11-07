# stack LIFO 

class Stack:
    def __init__(self):
        self.data = []  # internal list

    def push(self, value):
        self._data.append(value)
    
    def pop(self):
        if not self._data:
            raise.IndexError("pop from an empty stack")

    def peek(self):
        if not self.:
        return len(self._data) == 0
    
    def size(self):
        return len(self._data)

