'''
[-2,1,-3,4,-1,2,1,-5,4]
[5,4,-1,7,8]
[1]
[1,2]
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return p3(nums)
    
'''
TC = n
SC = 1
'''
def ans1(self, nums: List[int]) -> int:

    a = 0
    m = -sys.maxsize

    for n in nums:
        a += n

        if a < n:
            a = n
        if m < a:
            m = a

    return m

'''
TC = n
SC = 1
ans1 is better solution as it does not use else
'''
def p1(self, nums: List[int]) -> int:

    maxv = -sys.maxsize
    csum = 0

    for i in nums:

        if i+csum < i:
            csum = i
        else:
            csum += i

        if csum > maxv:
            maxv = csum

    return maxv

'''
TC = n
SC = 1
'''
def p2(self, nums: List[int]) -> int:

    t = 0
    m = -sys.maxsize

    for n in nums:

        t += n

        if n > t:
            t = n
        if t > m:
            m = t

    return m
        
'''
Kadane's Algo
TN = n, SC = 1
'''
def p3(nums):
    
    mx = nums[0]
    t = 0
    
    for n in nums:
        t += n
        
        if n > t:
            t = n
        if t > mx:
            mx = t
            
    return mx
    
        
        
        