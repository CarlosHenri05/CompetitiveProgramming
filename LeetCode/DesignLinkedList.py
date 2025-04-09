class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        

    def get(self, index):
        if not self.head:
            return -1

        i = 0
        current = self.head
        while current and i<index:
            current = current.next 
            i+=1

        
        if i!=index:
            return -1

        if current:
            return current.val
        else:
            return -1


    def addAtHead(self, val):
        new_node = Node(val)
        temp = self.head

        if not temp:
            self.head = new_node
            self.tail = new_node
        else:
          new_node.next = self.head
          self.head = new_node
          new_node.next = temp
          temp.prev = new_node

        

    def addAtTail(self, val):
        new_node = Node(val)
        temp = self.tail 

        if not temp:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            new_node.prev = temp
            temp.next = new_node
            new_node.next = None
        

    def addAtIndex(self, index, val):
        new_node = Node(val)

        if index==0:
            if not self.head:
              self.head = new_node
              self.tail = new_node
            else:
              new_node.next = self.head
              self.head.prev = new_node
              self.head = new_node

            return 
        
        current = self.head
        i = 0
        
        if not current and index!=0:
            return 
        

        while current and i<index:
            current = current.next
            i+=1

        if i != index:
          return
        
        
        if not current and i==index:
            
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        else:
          if current:
            temp = current
            prev_node = current.prev

            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = temp
            temp.prev = new_node

    def deleteAtIndex(self, index):

        if index==0:
            if self.head:
                if self.head.next:
                    self.head = self.head.next
                    self.head.prev = None
                else:
                    self.head = None 
          
            return

        current = self.head
        i = 0

        while current and i<index:
           current = current.next
           i+=1
        
        if i!=index:
           return

        if current==self.tail:
          self.tail = current.prev
          if self.tail:
            self.tail.next = None
          else:
             self.head = None

        
        if current:  
            if current.next!=None and i==index:
                prev_current = current.prev
                next_current = current.next
                prev_current.next = next_current
                next_current.prev = prev_current
                
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
