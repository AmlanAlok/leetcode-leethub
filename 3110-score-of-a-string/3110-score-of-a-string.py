class Solution:
    def scoreOfString(self, s: str) -> int:
        return ans(s)
    
def ans(s):
    
    i = 1
    N = len(s)
    score = 0
    
    while i < N:
        score += abs(ord(s[i]) - ord(s[i-1]))
        i += 1
    
    return score
    
'''
"hello"
"zaz"
'''