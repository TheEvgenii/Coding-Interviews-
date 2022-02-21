# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0);
        dummy.next = head
        count = 0
        
        newhead = head
        
        new1head = head
        
        
        while newhead:
            count +=1
            newhead = newhead.next
        count = count - n
        
        newhead = dummy
        while count > 0:
            newhead = newhead.next
            count -= 1
        newhead.next = newhead.next.next
        
        return(dummy.next)
        