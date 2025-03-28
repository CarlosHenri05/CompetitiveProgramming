class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        arr = []
        while list1:
            arr.append(list1.val)
            list1 = list1.next

        while list2:
            arr.append(list2.val)
            list2 = list2.next
        
        arr.sort()

        dummy = ListNode(-1)
        curr = dummy

        for value in arr:
            curr = ListNode(value)
            curr = curr.next  
        
        return dummy.next