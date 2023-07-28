'''
[3,2,3]
[2,2,1,1,1,2,2]
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return ans1(nums)
    
def ans1(nums):
    d={}
    
    for k in nums:
        if k in d:
            d[k] += 1
        else:
            d[k] = 1
    
    threshold = len(nums)/2
    
    for k, v in d.items():
        if v > threshold:
            max_k = k
    
    return max_k