'''
[1,1,0,1,1,1]
[1,0,1,1,0,1]
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return sol2(nums)
    
    
def sol2(nums):
    
    maxlen = 0
    c = 0
    
    for n in nums:
        if n == 1:
            c += 1
        if n == 0:
            maxlen = max(maxlen, c)
            c = 0
    
    return max(maxlen, c)

'''TC = n, SC = 1'''
def sol(nums):
    
    maxlen = 0
    c = 0
    
    for n in nums:
        
        if n == 1:
            c += 1
            maxlen = max(c, maxlen)
        if n == 0:
            c = 0
    
    return maxlen
                