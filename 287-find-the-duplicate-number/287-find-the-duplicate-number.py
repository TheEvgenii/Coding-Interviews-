class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashtable = {}
        for c in nums:
            if c in hashtable:
                hashtable[c] +=1
                return c
            else:
                hashtable[c] = 1
        
        