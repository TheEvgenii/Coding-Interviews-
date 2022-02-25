# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        dummy = None
        curr = None
        while head:
            
            
            if head.val != val:
                newhead = ListNode(0)
                newhead.val = head.val
                newhead.next = dummy 
                dummy = newhead
                head = head.next
                curr = newhead
                
            else:
                head = head.next
                
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt  
        return prev
            
        