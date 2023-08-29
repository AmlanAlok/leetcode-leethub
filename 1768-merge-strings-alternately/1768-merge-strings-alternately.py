'''
"abc"
"pqr"
"ab"
"pqrs"
"abcd"
"pq"
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ans2(word1, word2)
    
'''
Two Pointer Approach
TC = m+n
SC = 1 
'''
def ans1(word1, word2):
    
    ans = ''
    i,j = 0, 0
    
    while i < len(word1) or j < len(word2):
        
        if i < len(word1):
            ans += word1[i]
            i += 1
        if j < len(word2):
            ans += word2[j]
            j += 1
            
    return ans

'''
One-Pointer
TC = max(m, n)
SC = 1
'''
def ans2(word1, word2):
    
    m, n = len(word1), len(word2)
    ans = ''
    mx = max(m, n)
    
    for i in range(mx):
        if i < m:
            ans += word1[i]
        if i < n:
            ans += word2[i]
    
    return ans
    
    
    
    
    
    
    
    
    
    
    
            
        
        
        