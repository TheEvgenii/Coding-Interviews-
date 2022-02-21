class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        count = 0
        newarr = []
        for i in nums:
            if i not in newarr:
                newarr.append(i)
                countnums = nums.count(i)
                if countnums > count:
                    count = countnums
                    res = i
        return res
        