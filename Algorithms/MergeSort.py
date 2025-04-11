class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node_7 = ListNode(7)
node_1 = ListNode(1, next=node_7)
node_3 = ListNode(3,next= node_1)
node_9 = ListNode(9, next= node_3)


def findMiddle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def mergeLists(l1,l2):
    head = ListNode()
    tail = head
    while l1 and l2:
        if l1.val<l2.val:
            tail.next = l1
            l1 = l1.next 
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return head.next

def mergeSort(head):
    if not head or not head.next:
        return head

    middle = findMiddle(head)

    after_middle = middle.next 
    middle.next = None

    left = mergeSort(head)
    right = mergeSort(after_middle)

    sorted_list = mergeLists(left,right)

    return sorted_list


my_list = mergeSort(node_9)

