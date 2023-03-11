class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        return self.ans1(s)
    
    def ans1(self, s: str) -> int:
        
        i = len(s)-1
        count = 0
        
        while s[i] == ' ' and i >= 0:
            i -= 1
        
        while i >= 0:
            c = s[i]
            
            if c is not ' ':
                count += 1
            else:
                break
            
            i -= 1
        
        return count
                
        