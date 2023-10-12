class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return ans1(nums)
    
def ans1(nums):
    
    d = {}
    
    for n in nums:
        if n in d:
            return True
        else:
            d[n] = 1
            
    return False