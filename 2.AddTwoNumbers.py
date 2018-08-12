# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_list = []
        l2_list = []

        while l1:
            l1_list.append(l1.val)
            l1 = l1.next

        while l2:
            l2_list.append(l2.val)
            l2 = l2.next    

        l1_to_be_sum = [l1_list[i]*(10**i) for i in range(len(l1_list))]
        l2_to_be_sum = [l2_list[i]*(10**i) for i in range(len(l2_list))]
        sum_num = sum(l1_to_be_sum)+sum(l2_to_be_sum)
        sum_str = str(sum_num)
        sum_list = list(sum_str)[::-1]
        return [int(i) for i in sum_list]
                
