'''
[0,1,0,3,12]
[0]
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return ans1(nums)
    
def ans1(nums):

    i, j = 0, 0
    
    while i < len(nums):
        
        if nums[i] == 0:
            while j < len(nums):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                j+=1
        i += 1
        j = i
    
        
        
    