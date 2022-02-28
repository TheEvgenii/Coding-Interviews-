class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start = end = 0 
        while end < len(nums):
            while end + 1 < len(nums) and nums[end] + 1 == nums[end+1] :
                end = end + 1
            
            if nums[start] != nums[end] : 
                result.append(f"{str(nums[start])}->{str(nums[end])}")
            else : 
                result.append(str(nums[start]))
            
            end = end + 1 
            start = end
        return result
        