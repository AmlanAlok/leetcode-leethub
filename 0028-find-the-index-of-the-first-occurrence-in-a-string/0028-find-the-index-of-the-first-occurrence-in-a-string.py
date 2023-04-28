'''
"sadbutsad"
"sad"
"leetcode"
"leeto"
"aaa"
"aaaa"
"mississippi"
"issip"
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return p1(haystack, needle)

def p1(x, y):
    
    l1, l2 = len(x), len(y)
    
    last_idx = l1-l2
    
    for i in range(last_idx+1):
        st = x[i:i+l2]
        if st == y:
            return i
    return -1
    
    
    
    
    
'''Sliding window sol - TC = O(nm), SC = O(1)'''
def ans2(x, y):
    m, n = len(y), len(x)
    last_idx = n-m
    for start in range(last_idx+1):
        for i in range(m):
            if y[i] != x[start + i]:
                break
            if i == m-1:
                return start
            
    return -1
    

'''My first attempt: My sliding window code'''
def ans1(x: str, y : str):
    
    if len(y) > len(x):
        return -1
    i = 0
    
    while i < len(x):
        j = 0
        
        k = i
        try:
            while x[k+j] == y[j] and j < len(y) and i < len(x):
                # i += 1
                j += 1
                if j == len(y):
                    # print(k, len(y))
                    # return i - len(y)
                    return k
        except Exception as e:
            print(i, j, k)
            print(e)
    
        i+=1
    
    return -1
        