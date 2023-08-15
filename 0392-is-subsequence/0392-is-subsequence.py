'''
"abc"
"ahbgdc"
"axc"
"ahbgdc"
""
"ahbgdc"
""
""
"acb"
"ahbgdc"
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return ans2(s, t)

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


def ans2(s, t):
    
    d = {}
    
    for i in range(len(t)):
        v = t[i]
        
        if v in d:
            d[v].append(i)
        else:
            d[v] = [i]
    print(d)
    t = -1
    
    for c in s:
        
        if c in d:
            idx = d[c]
            
            '''Using linear search to find appropiate index'''
            
            if idx[-1] > t:
                for n in idx:
                    if n > t:
                        t = n
                        break
            else:
                return False        # if there are no idx values that are larger than t
            
        else:
            return False
    
    return True
            
        
            
    
    
    
    
    
        