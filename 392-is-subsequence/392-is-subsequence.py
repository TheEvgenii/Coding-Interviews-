class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        l = len(s)
        l2 = len(t)
        if s == "":
            return True
            
        for c in t:
            if c == s[i]:
                i+= 1
                if l ==i:
                    return True
        return False

        