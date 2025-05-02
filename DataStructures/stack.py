class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
  
class Stack:
  def __init__(self):
    self.top = None
    self.size = 0
  
  def is_empty(self):
    if self.size == 0:
      return True
    return False
  
  def size(self):
    return self.size
  

  def peek(self):
    if self.is_empty:
      return None
    
    return self.top.next


  def push(self, val):
    new_node = Node(val)
    new_node.next = self.top.next
    self.top.next = new_node
    self.size += 1
