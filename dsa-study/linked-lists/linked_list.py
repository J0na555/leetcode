class Node:
    def __init__(self, data):
        self.data = data   # stores the value
        self.next = None   # stores the next Node


class LinkedList:
    def __init__(self):
        self.head = None # first node of the LinkedList
        # if the head is empty then that means the linkedlist is empty

    
    def insert_at_the_beginning(self, data):
        new_node = Node(data)
        new_node.next = head
        self.head = new_node
        # o(1) time complexity

    # travers until next == none and attack a new node there
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        # time complexity o(n) cause we traverse the whole list 
    

    # show the linked list 
    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")
      
    def delete(self, key):
        current = self.head

        # case 1: head is the key
        if current and current.data == key:
            self.head = current.next
            return

        # case 2: search for the key
        prev = None
        if current and current.data != key:
            prev = current
            current = current.next

        # case 3 key not found 
        if current is None:
            print("value not found")
            return
        
        prev.next = current.next

    


    def search(self, key):
        current = self.head
        position = 0

        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1

        return -1
    


    def reverse(self):
        prev = None       # 1. 'prev' starts as None, will track the node *behind* 'current' (initially, nothing is behind the first node)
        current = self.head # 2. 'current' starts at the head, iterating through the original list

        while current:
            next_node = current.next  # 3. Store the original 'next' node of 'current' before changing 'current.next'
            current.next = prev       # 4. Reverse 'current's pointer to point to 'prev' (the node that was just processed)
            prev = current            # 5. Move 'prev' forward to become the 'current' node for the next iteration
            current = next_node       # 6. Move 'current' forward to the 'next_node' (which was saved in step 3)

        self.head = prev  # 7. Once 'current' is None (end of list), 'prev' will be the last node of the original list, which is the new head.
