class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_array = []
        for i in range (len(nums)):
            new_array.append(nums[i] * nums[i])
               
        return sorted(new_array)
            
            
        
        