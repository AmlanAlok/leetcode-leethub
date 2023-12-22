class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        return dec21(s, k)
    
def ans1(s, k):
    d = {}
    l = r = 0
    
    res = 0
    
    # while l < len(s) and r < len(s):
    for r in range(len(s)):
        
        d[s[r]] = d.get(s[r], 0) + 1
        
        # max(d.values()) is TC = O(26)
        while (r-l+1) - max(d.values()) > k:
            d[s[l]] -= 1
            l += 1
        
        res = max(res, (r-l+1))
        
        r += 1
    
    return res

def ans2(s, k):
    d = {}
    l = r = 0
    
    res = 0
    maxf = 0
    
    # while l < len(s) and r < len(s):
    for r in range(len(s)):
        
        d[s[r]] = d.get(s[r], 0) + 1
        maxf = max(maxf, d[s[r]])
        
        # max(d.values()) is TC = O(26)
        while (r-l+1) - maxf > k:
            d[s[l]] -= 1
            l += 1
        
        res = max(res, (r-l+1))
        
        # r += 1
    
    return res

def dec21(s, k):
    
    i = j = 0
    d = {}
    mx = 0
    
    for j in range(len(s)):
        c = s[j]
        
        d[c] = d.get(c, 0) + 1
        
        if (j-i+1) - max(d.values()) > k:
            z = s[i]
            d[z] -= 1
            i += 1
        
        mx = max(mx, (j-i+1))
    
    return mx
    
        
