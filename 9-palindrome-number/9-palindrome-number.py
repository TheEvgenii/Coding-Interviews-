class Solution:
    def isPalindrome(self, x: int) -> bool:
        palendrome = str(x)
        reverse = palendrome[::-1] 
        if palendrome == reverse:
            return True
        else:
            return False
        #if x<0 or x % 10 = 0 and x != 0:
        #    return false
        #
        #revertnum = 0
       # while x > revertnum:
        #    revertnum = revertnum * 10 + x % 10
       #     x /= 10
            
        #
       # return x = revertnum or x = revertnum/10
        
        