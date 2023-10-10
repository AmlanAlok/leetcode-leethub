class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        return ans1(s, k)
    
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
        