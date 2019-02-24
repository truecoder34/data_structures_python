'''
    define SinglyLinkedList class
    here are realization of all methods of SinglyLinkedList
'''
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
    # DON T WORK WELL
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

    # Find elem in list by name
    def findElemByNodeValue(self, valueToFind):
        if self == None:
            return (None)
        #NodeToFind = Node(value)
        CurrentNode = self.headNode
        while CurrentNode is not None:
            if(CurrentNode.value == valueToFind):
                return (CurrentNode)
            else:
                CurrentNode = CurrentNode.next
                #self.headNode = CurrentNode

    '''
        P5. Add two linked lists from left to right
        e.g. 1->2->3 + 8->7 => 321+78 = 399
    '''
    def sum_linked_lists_backward(self, list1, list2):
        carry_over = 0
        head = Node(0)
        poonter = head
        digit = 0
        # until all lists exists, sum elems
        while list1 != None and list2 != None:
            sum_ = list1.val + list2.val + carry_over
            pointer.next = Node(sum_ % 10)
            pointer = pointer.next
            carry_over = sum_ / 10
            list1 = list1.next
            list2 = list2.next

        if list1 == None:
            while list2 != None:
                sum_ = list2.val + carry_over
                pointer.next = Node(sum_ % 10)
                pointer = pointer.next
                carry_over = sum_ / 10
                list2 = list2.next

        if list2 == None:
            while list1 != None:
                sum_ = list1.val + carry_over
                pointer.next = Node(sum_ % 10)
                pointer = pointer.next
                carry_over = sum_ / 10
                list1 = list1.next
        if carry_over > 0:
            pointer.next = Node(carry_over)
        return head.next



