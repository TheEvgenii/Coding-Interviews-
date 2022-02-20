class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        newarr = []
        res = 0
        for i in heights:
            newarr.append(i)
        newarr.sort()
        for i in range (len(newarr)):
            if newarr[i] != heights[i]:
                res+=1
        print(newarr)
        return res
        
        