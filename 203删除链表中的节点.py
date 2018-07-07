class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return
        new_head = ListNode(0)
        new_head.next = head
        pre = new_head
        current = head
        while current:
            if current.val == val:
                pre.next = current.next
            else:
                pre = pre.next
            current = current.next
            
        return new_head.next
        
