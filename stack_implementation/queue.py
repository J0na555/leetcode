# FIFO

from collections import deque

class Queue:
    def __init__(self):
        self._d = deque()

    def enqueue(self, value):
        self._d.append(value)

    def deque(self):
        if not self._d:
            raise IndexError("deque from an empty Queue")
        return self._d.popleft()

    def peek(self):
        return self._d[0] if self._d else None  
        
    def isEmpty():
        return not self._d
