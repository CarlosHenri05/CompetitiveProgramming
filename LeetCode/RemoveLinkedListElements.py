# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):

        if not head:
            return None

        while head and head.val == val: # -> This means the head node is the one we want to remove, so we move the head pointer forward.
            head = head.next

        current = head


        while current and current.next:  # -> This means we are at the current node, and we need to check if the next node is the one we want to remove.
            if current.next.val == val:
                current.next = current.next.next # -> We skip it if it is the one we want to remove.
            else:
                current = current.next # -> We move the current pointer forward if the next node is not the one we want to remove.
        
        return head 

        