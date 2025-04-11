class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from math import gcd

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        current = head

        while current and current.next:
            gcd_value = gcd(current.val, current.next.val) # maximo divisor comum para o numero atual e o proximo
            gcd_node = ListNode(gcd_value)

            gcd_node.next = current.next # Como temos que adicionar o gcd no meio dos dois, basta apontarmos o gcd_node.next como o current.next anterior
            current.next = gcd_node # e o current.next sendo o gcd_node

            current = gcd_node.next # depois, pulamos o nodo do divisor comum para o numero que era da lista original
            

        
        return head

# [18,3,6,10,3]






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
