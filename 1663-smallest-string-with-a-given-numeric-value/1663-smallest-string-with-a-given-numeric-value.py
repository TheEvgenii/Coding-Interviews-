class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        lookup = {i: chr(char) for i,char in enumerate(range(ord('a'),ord('z')+1))}
        tmp = [0 for _ in range(n)]
        
        end = len(tmp)-1
        left = k -(len(tmp))
        
        while left>0 and end >=0:
            if left > 25:
                tmp[end] = 25
                left -= 25
            else:
                tmp[end] = left
                left = 0
            end -=1
        return "".join([lookup[i] for i in tmp])
        