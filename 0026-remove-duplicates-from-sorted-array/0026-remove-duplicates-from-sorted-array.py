class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return dec26(nums)
    
def ans1(nums):
    ''' TC = n, SC = 1 '''
    i, j = 0, 1
    l = len(nums)
    
    while i < l and j < l:
        
        if nums[j] != nums[i]:
            i+=1
            nums[i] = nums[j]
        j+=1
        
    return i+1
        
def dec26(nums):
    
    i = j = 0
    cur = nums[i]
    
    for j in range(len(nums)):
        n = nums[j]
        
        if n > cur:
            i += 1
            nums[i] = n
            cur = n
    
    return i+1
        
        
    

        