'''
[1,2,2,1,1,3]
[1,2]
[-3,0,1,-3,1,1,1,-3,10,0]
'''

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return ans2(arr)
    
def ans2(arr):
    d = {}
    
    for n in arr:
        d[n] = d[n]+1 if n in d else 1
    
    v = d.values()
    
    if len(v) == len(set(v)):
        return True
    return False
        
def ans1(arr):
    d = {}
    for n in arr:
        d[n] = d[n] + 1 if n in d else 1

    vd = {}

    for v in list(d.values()):
        if v in vd:
            return False
        else:
            vd[v] = 1

    return True
                