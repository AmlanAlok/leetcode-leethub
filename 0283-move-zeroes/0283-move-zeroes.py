'''
[0,1,0,3,12]
[0]
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return ans2(nums)
    
    
def ans2(nums):
    
    j = -1
    
    for i in range(len(nums)):
        if nums[i] != 0:
            j += 1
            nums[i], nums[j] = nums[j], nums[i]
            
        

    
def ans1(nums):
    
    c = 0
    
    for v in nums:
        if v != 0:
            c += 1

    i, j = 0, 0
    
    while i < len(nums):
        if i == c:
            break
        if nums[i] == 0:
            while j < len(nums):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                j+=1
        i += 1
        j = i
        
        
    
        
        
    