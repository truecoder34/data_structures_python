from Node import Node
from SinglyLinkedList import SinglyLinkedList

SinglyList = SinglyLinkedList()
SinglyList.headNode = Node("Monday")            # Set FIRST elem in linked list

node2 = Node("Tuesday")
node3 = Node("Wednesday")

# Linking nodes
SinglyList.headNode.next = node2
node2.next = node3

# print all list elems
SinglyList.traverse()
print("---------------------------------------")

# INSERT elem AT THE BEGINNING to linked list
SinglyList.insertAtBeginning("Sunday")
SinglyList.traverse()
print("---------------------------------------")
# INSERT elem AT THE END to linked list
SinglyList.insertAtTheEnd("Saturday")
SinglyList.traverse()
print("---------------------------------------")

SinglyList.insertBetween(SinglyList.headNode.next, "Friday")
SinglyList.traverse()
print("---------------------------------------")

SinglyList.insertBetween(SinglyList.headNode.next.next, "Thursday")
SinglyList.traverse()
print("---------------------------------------")


SinglyList.removeNode("Thursday")
SinglyList.traverse()
print("---------------------------------------")

SinglyList.removeNode("Sunday")
SinglyList.traverse()
print("---------------------------------------")
print("---------------------------------------")
print("---------------------------------------")

# Remove duplicates from linked list
SinglyList.insertAtTheEnd("Saturday")
SinglyList.insertAtTheEnd("Wednesday")
SinglyList.insertAtTheEnd("Tuesday")
SinglyList.traverse()
SinglyList.removeDuplicates()
print("---------------------------------------")
SinglyList.traverse()

print("---------------------------------------")
print("---------------------------------------")
print("---------------------------------------")
print("---------------------------------------")
print(SinglyList.findElemByNodeValue("Saturday"))

