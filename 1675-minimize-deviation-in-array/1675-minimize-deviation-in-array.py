class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        h = []
        for n in nums:
            mn = mx = n
            while mn%2==0:
                mn //= 2
            if mx%2!= 0:
                mx *=2
                    
            heappush(h,(mn,mx))
                
        MX = max([i for i,j in h])
        output = float('inf')
        
        while len(h)==len(nums):
            x,limit = heappop(h)
            output = min(output,MX-x)
            if x < limit:
                heappush(h,(x*2,limit))
                MX = max(MX,x*2)
        return output
        