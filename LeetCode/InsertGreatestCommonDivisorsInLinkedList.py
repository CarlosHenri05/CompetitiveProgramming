from math import gcd

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        current = head

        while current and current.next:
            gcd_value = gcd(current.val, current.next.val)
            gcd_node = ListNode(gcd_value)

            gcd_node.next = current.next 
            current.next = gcd_node

            current = gcd_node.next
            

        
        return head
