class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        N = len(s)
        S = list(s)
        
        for i in range (N):
            if S[i] == "(":
                stack.append(i)
                
            elif S[i] == ")":
                if stack:
                    stack.pop()
                else:
                    S[i] = ""
        for j in stack:
            S[j] = ""
            
        return "".join(S)
        
        
        