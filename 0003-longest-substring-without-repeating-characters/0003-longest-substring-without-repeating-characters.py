'''
"abcabcbb"
"bbbbb"
"pwwkew"
"abba"
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return ans2(s)
    
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

'''
TC = n
SC = O(min(m, n))  = We need O(k). k is the size of dict or set.
n is the length of string. worst case when all chars are unique.
m are the num of chars in the alphabet.
'''
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

def ans2(s):
    i = j = 0
    d = {}
    ans = 0
    
    while j <len(s):
        c = s[j]
        
        if c in d and d[c] >= i:
            i = d[c] + 1
        else:
            ans = max(ans, j-i+1)
        
        d[c] = j
        j += 1
    
    return ans
        
        
        
            