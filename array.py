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
        