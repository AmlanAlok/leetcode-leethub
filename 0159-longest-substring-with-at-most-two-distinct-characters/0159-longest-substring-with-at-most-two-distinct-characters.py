class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        return dec19(s)
    
def dec19(s):
    
    mx = 0
    l = len(s)
    j = 0
    d = {}
    
    for j in range(l):
        
        c = s[j]
        
        d[c] = d.get(c, 0) + 1
        
        if len(d) <= 2:
            mx += 1
        else:
            i = j - mx
            z = s[i]
            d[z] -= 1
            if d[z] == 0:
                del d[z]
        
    return mx
        
    