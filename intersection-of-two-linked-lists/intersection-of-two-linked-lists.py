# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB) :
        hashset = set()
        
        while headB is not None:
            hashset.add(headB)
            headB = headB.next
            
        while headA is not None:
            if headA in hashset:
                return headA
            headA = headA.next
            
        return None
        