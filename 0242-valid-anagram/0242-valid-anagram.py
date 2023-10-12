'''
"anagram"
"nagaram"
"rat"
"car"
'''
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return oct12(s, t)
    
    '''
    TC = n
    SC = n+m
    '''
    def old1(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
            
        d = {}
        
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        
        for c in t:
            if c in d and d[c] > 0:
                d[c] -= 1
            else:
                return False
        
        return True
    
    def old2(self, s: str, t: str) -> bool:
        source = Counter(s)
        target = Counter(t)
        print(source)
        print(target)
        return True if source == target else False
'''TC = n, SC = 1, My first attempt'''                
def oct12(s, t):
    
    a = [0] * 26
    
    for c in s:
        idx = ord(c) - ord('a')
        a[idx] += 1
    
    for c in t:
        idx = ord(c) - ord('a')
        a[idx] -= 1
        
    for n in a:
        if n != 0:
            return False
    return True
    
    
    
    
    