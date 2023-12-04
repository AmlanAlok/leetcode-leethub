'''
[1,2,3,4]
[1,1,1,1,1]
[3,1,2,10,1]
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return dec03(nums)
    
def dec03(nums):
    
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    
    return nums