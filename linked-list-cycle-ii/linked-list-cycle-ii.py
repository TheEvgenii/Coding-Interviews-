class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """   
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return head
            nodes_seen.add(head)
            head = head.next
        return None