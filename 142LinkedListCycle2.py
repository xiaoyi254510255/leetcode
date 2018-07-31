#不适用额外空间
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head==None or head.next == None or head.next.next == None):
            return None
        fast = head.next.next
        slow = head.next
        while(fast != slow):
            if(fast.next==None or fast.next.next==None):
                return None
            fast = fast.next.next;
            slow = slow.next;
        fast = head;
        while(fast!=slow):
            fast = fast.next;
            slow = slow.next;
        return slow;
        
#使用set，使用了额外的空间
class Solution2(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return None
        nod_set = set()
        
        while head not in nod_set:
            
            if not head:
                return None
            nod_set.add(head)
            
            head = head.next
        
        return head
        
