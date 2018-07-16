# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or (not head.next):
            return None
        nod = head
        nod_list = []
        while nod:
            nod_list.append(nod)
            nod = nod.next
        
        if n == len(nod_list):
            return head.next
        if n == 1:
            nod_list[-2].next = None
        else:
            nod_list[-n-1].next = nod_list[-n+1]
        return head
        
