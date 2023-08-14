'''
"abc"
"ahbgdc"
"axc"
"ahbgdc"
""
"ahbgdc"
""
""
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return ans1(s, t)

def ans1(s, t):
    
    if s == '':
        return True
    
    i, j = 0, 0
    
    while j < len(t):
        
        if s[i] == t[j]:
            i+=1
            if i == len(s):
                return True
        j+=1
    
    return False
        