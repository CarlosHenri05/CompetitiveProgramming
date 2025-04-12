# Resolução com algoritmo de Floyd
# (Tortoise and Hare)

class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

            # Quando os dois estiverem no mesmo lugar, vamos resetar o slow
            if slow==fast:
                slow = head 
                while slow!=fast:
                    # Depois vamos fazer se encontrarem de novo, quando se encontrarem retorne
                    # o slow ou o fast, tanto faz
                    slow = slow.next
                    fast = fast.next 
                return slow
