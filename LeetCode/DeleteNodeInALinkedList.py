# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Achei essa questão meio trivial, mas
# como o problema não quer que realmente apagamos o nó,
# basta deslinkar ele da lista 
class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val 
        node.next = node.next.next
        
        