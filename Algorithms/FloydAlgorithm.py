class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self, head=None):
    self.head = head
    self.tail = head

# This algorithm uses two pointers (slow and fast) to detect cycles or find the middle of a linked list.
def tortoiseAndHare(head):
    slow = head.next 
    fast = head.next.next 

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
  
    return slow

# Create some linked list nodes for testing
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Link the nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  # Create a cycle for testing

# Return the head of the linked list
