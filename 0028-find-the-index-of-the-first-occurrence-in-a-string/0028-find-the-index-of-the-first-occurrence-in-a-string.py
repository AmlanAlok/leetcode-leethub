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
        return ans1(haystack, needle)
    
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
        