'''
[3,2,3]
[2,2,1,1,1,2,2]
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return ans1(nums)
    
def old1(nums):
    d={}
    
    for k in nums:
        if k in d:
            d[k] += 1
        else:
            d[k] = 1
    
    threshold = len(nums)/2
    
    for k, v in d.items():
        if v > threshold:
            max_k = k           # as the threshold is greater than half of length, we do not need to 
    
    return max_k

'''
TC = n
SC = n
'''
def ans1(nums):
    
    d = {}
    
    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    
    threshold = len(nums)/2
    
    for k, v in d.items():
        if v > threshold:
            return k
        