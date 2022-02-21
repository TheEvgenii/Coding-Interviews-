class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        newarr = []
        maxnum = 0
        for i in nums:
            if i not in newarr:
                newarr.append(i)
        newarr.sort(reverse=True)
        if (len(newarr)) < 3:
            return max(nums)
        return newarr[2]
        