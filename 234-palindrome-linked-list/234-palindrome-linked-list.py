# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        arr1 = []
        
        
        
        
        
        prev = None   
        res = head
        curr = head
        
    
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            arr1.append(prev.val)
            curr = nxt
        if arr1 == arr1[::-1]:
            return True
        else:
            return False
        