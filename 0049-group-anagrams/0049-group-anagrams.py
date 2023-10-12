'''
[""]
["a"]
["hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"]
["eat","tea","tan","ate","nat","bat"]
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return oct12(strs)
    
'''This will work in python 3.7 or later.
Dictionaries are ordered from Python 3.7 onwards
I changed the logic to adjsut for unordered dictionaries.
'''
'''TC = nk, SC = n'''
def oct12(strs):
    
    z = {}
    
    for st in strs:
        
        a = [0]*26
        
        '''TC = O(100) or O(K)'''
        for c in st:
            idx = ord(c) - ord('a')
            # d[c] = d.get(c, 0) + 1
            a[idx] += 1
        
        new_k = ''
        for i in range(26):
            ch = chr(97 + i)
            new_k += ch + str(a[i])
            # new_k += ord(k) + v
        
        # print(new_k)
        if new_k in z:
            z[new_k].append(st)
            # print(z[new_k])
        else:
            z[new_k] = [st]
    
    
    ans = []
    
    for k, v in z.items():
        ans.append(v)
    
    return ans
        

def oct13(strs):
    
    z = {}
    
    for st in strs:
        
        a = [0]*26
        
        '''TC = O(100) or O(K)'''
        for c in st:
            idx = ord(c) - ord('a')
            a[idx] += 1
        
        new_k = tuple(a)
        
        # print(new_k)
        if new_k in z:
            z[new_k].append(st)
            # print(z[new_k])
        else:
            z[new_k] = [st]
    
    return z.values()