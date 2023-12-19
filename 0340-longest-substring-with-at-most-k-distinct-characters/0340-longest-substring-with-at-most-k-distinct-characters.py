'''
"a@b$5!a8alskj234jasdf*()@$&%&#FJAvjjdaurNNMa8ASDF-0321jf?>{}L:fh"
10
"a"
2
"eceba"
2
"aa"
1
"araaci"
2
"araaci"
1
"cbbebi"
3
'''

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        return dec18(s, k)
    

def ans1(s: str, k: int) -> int:
    '''TC = 1, SC = k+1'''
    i = j = a = 0
    m = 0
    d = {}
    l = len(s)
    # s = s.lower() # caused problem in test case = "a@b$5!a8alskj234jasdf*()@$&%&#FJAvjjdaurNNMa8ASDF-0321jf?>{}L:fh"
    
    while j < l:
        
        while len(d.items()) <= k and j < l:
            c = s[j]
            
            if c in d:
                d[c] += 1
            else: 
                d[c] = 1
        
            if len(d.items()) <= k:
                if (j-i+1) > m:
                    m = j-i+1
            
            j+=1
            
        while i < l and len(d.items()) > k :
            if s[i] in d:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    del d[s[i]]
                    # break
            i+=1
    
    return m

def dec18(s, k):
    
    l = len(s)
    i = j = 0
    d = {}
    mx = 0
    
    while j < l:
        
        while j < l and len(d.items()) <= k:
            c = s[j]
            
            d[c] = d.get(c, 0) + 1
            
            if len(d.items()) <= k:
                long = j-i+1
                if long > mx:
                    mx = long 
            
            j += 1
        
        while i < l and len(d.items()) > k:
            c = s[i]
            
            d[c] -=1
            
            if d[c] == 0:
                del d[c]
            
            i += 1
            
    return mx
    
        
        
        
        