class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_table = {}
        
        for num in nums:
            hash_table[num] = 1
            
        res = []
        
        for num in range(1, len(nums) + 1 ):
            if num not in hash_table:
                res.append(num)
        return res
        
        
        