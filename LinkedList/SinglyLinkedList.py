from Node import Node

class SinglyLinkedList:
    def __init__(self):
        self.headNode = None        # SET HEAD NODE

    # Traverse method/ PRINT LIST METHOD
    def traverse(self):
        node = self.headNode       # start from head node
        while node != None:
            print(node.value)         # print current node value
            node = node.next        # set pointer to next elem

    # INSERT elem AT THE BEGINNING to linked list
    def insertAtBeginning(self, newValue):
        NewNode = Node(newValue)
        # Update the new nodes next val to existing node
        NewNode.next = self.headNode
        self.headNode = NewNode

    # INSERT elem AT THE END to linked list
    def insertAtTheEnd(self, newValue):
        NewLastNode = Node(newValue)
        # if LINKED LIST IS EMPTY - set new node as the head node
        if self.headNode == None:
            self.headNode = NewLastNode
            return
        # traverse list to find LAST elem
        node = self.headNode            # initialize last variable with 1 node
        while node.next != None:
            node = node.next

        node.next = NewLastNode         # Set link to new last node


    # Insert between 2 nodes
    def insertBetween(self, middle_node, newValue):
        if middle_node is None:
            print("The mentioned (Middle) node is absent")
            return

        NewNode = Node(newValue)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    # Remove node from list.
    # Node in LinkedList will be found by VALUE
    def removeNode(self, valueToRemove):
        HeadNode = self.headNode
        if (HeadNode != None):
            if (HeadNode.value == valueToRemove):
                self.headNode = HeadNode.next
                HeadNode = None
                return
        while (HeadNode != None):
            if (HeadNode.value == valueToRemove):
                break
            previousNode = HeadNode
            HeadNode = HeadNode.next

        if (HeadNode == None):
            return

        previousNode.next = HeadNode.next
        HeadNode = None

    # Remove duplicates from linked list
    def removeDuplicates(self):
        els = []
        node = self.headNode
        previousNode = None
        while node != None:
            if node.value in els:
                previousNode.next = node.next
            else:
                els.append(node.value)
            previousNode = node
            node = node.next

