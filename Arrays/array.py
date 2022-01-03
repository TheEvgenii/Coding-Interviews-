#123
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
            
        return nums



class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        
        return (ans)



class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ans = nums * 2
        return ans


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for i in range (len(operations)):
            if operations[i] == "++X" or operations[i] == "X++":
                ans = ans + 1
            if operations[i] == "--X" or operations[i] == "X--":
                ans = ans - 1
        return ans
        

        class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        d = 0
        for i in range(0,n):
            ans.append(nums[i])
        for b in range(n, len(nums)):
            ans.insert(d+1,nums[b])
            d = d+2
        return ans


        class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0
        fulltotal = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                total = total + 1
            if total > fulltotal:
                    fulltotal = total
            if nums[i] != 1:
                total = 0 
        return fulltotal 


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        str_num = map(str, nums)
        count = 0
        for s in str_num:
            if len(s) % 2 == 0:
                count += 1
        return count  


        class Solution:
        def sortedSquares(self, nums: List[int]) -> List[int]:
        new_array = []
        last_array = []
        for i in range (len(nums)):
            new_array.append(nums[i] * nums[i])
               
        return sorted(new_array)


        class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Write the elements of num2 into the end of nums1.
        for i in range(n):
            nums1[i + m] = nums2[i]
        
        # Sort nums1 list in-place.
        nums1.sort()