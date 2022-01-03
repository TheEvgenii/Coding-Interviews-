class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #n-1 
        indegree = [0] * (n+1) 
        outdegree = [0] * (n+1)
        
        for a,b in (trust):
            indegree[b] += 1
            outdegree[a] += 1
        for i in range (1, n+1):
            if outdegree[i] == 0 and indegree[i] == n-1:
                return i
        return -1
            