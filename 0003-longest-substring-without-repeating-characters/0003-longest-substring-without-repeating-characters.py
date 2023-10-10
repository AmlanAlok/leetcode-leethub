'''
"abcabcbb"
"bbbbb"
"pwwkew"
"abba"
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return ans1(s)
    
def old1(self, s: str) -> int:  
    m = 0
    q = 0
    d = {}
    a = []

    for i in range(len(s)):
        c = s[i]

        if c in d:
            pass
        else:
            a.append(c)

def ans1(s):
    
    i = j = 0
    d = {}
    ans = 0
    
    while j < len(s):
        c = s[j]
        
        if c not in d:
            d[c] = j
        else:
            i = max(d[c] + 1, i)    # so that i does not go back to an old index 0 "abba"
            d[c] = j        # updating index with latest occurrence
        
        ans = max(ans, j-i+1)
        
        j += 1
    
    return ans
            
            