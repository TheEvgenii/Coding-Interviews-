class Solution(object):
    def isValid(self, s):
        stack = []
        
        mapping = { "}": "{", ")": "(", "]": "["}
        
        for char in s:
            if char in mapping:

                top_elemet = stack.pop() if stack else '#' 
                
                if mapping[char] != top_elemet:
                    return False
                
            else:
                stack.append(char)
                    
        return not stack
        
        