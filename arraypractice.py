def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = 0 

        for i in range (len(nums)):
            if nums[i] != val:
                length = length +1
            return length
              
    
                
        
        
#qdddff
removeElement([3,2,2,3], 3)