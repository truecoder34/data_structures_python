#define doublyNode class - elem for doubly linked list
class DoublyNode:
    def __init__(self, val):
        self.value = val
        self.previous = None
        self.next = None