class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]
        
        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray


#class Solution:
#    def maxSubArray(self, nums: List[int]) -> int:
#        max_subarray = -math.inf
#        for i in range(len(nums)):
#            current_subarray = 0
#            for j in range(i, len(nums)):
#                current_subarray += nums[j]
#               max_subarray = max(max_subarray, current_subarray)
#        
#        return max_subarray                       
                       