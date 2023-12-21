'''
"abcabcbb"
"bbbbb"
"pwwkew"
"abba"
"abcdeafbdgcbb"
" "
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return dec20(s)
    
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
    '''
    TC = n
    SC = O(min(m, n))  = We need O(k). k is the size of dict or set.
    n is the length of string. worst case when all chars are unique.
    m are the num of chars in the alphabet.
    '''
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
        
def dec20(s):
    
    i = j = 0
    d = {}
    mx = 0
    
    for j in range(len(s)):
        
        c = s[j]
        
        if c not in d:
            d[c] = j
        else:
            i = max(d[c]+1, i)
            d[c] = j
            
        mx = max(mx, j-i+1) # this +1 helped to resolve " " case
        '''
        It corrects the +1 added earlier to i
        If all chars are unique, the +1 gives the length with 0-indexed arrays
        '''
        
    return mx

            