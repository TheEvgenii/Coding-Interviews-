class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        # Make a Set with the input.
        nums = set(nums)

        # Find the maximum.
        maximum = max(nums)

        # Check whether or not this is a case where
        # we need to return the *maximum*.
        if len(nums) < 3:
            return maximum

        # Otherwise, continue on to finding the third maximum.
        nums.remove(maximum)
        second_maximum = max(nums)
        nums.remove(second_maximum)
        return max(nums)
        