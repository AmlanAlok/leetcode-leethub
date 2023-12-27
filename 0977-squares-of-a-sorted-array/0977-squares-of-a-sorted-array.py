class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return dec26(nums)
    
def ans1(nums):
    
    i, j = 0, len(nums)-1
    
    ans = [None] * len(nums)
    k = len(nums)-1
    
    while i <= j:
        
        left, right = abs(nums[i]), abs(nums[j])
        
        if right > left:
            ans[k] = right**2
            j-=1
        else:
            ans[k] = left**2
            i+=1
        k-=1
        
    return ans
    
def dec26(nums):
    
    l = len(nums)
    ans = [None] * l
    
    j = l-1
    i = 0
    k = l-1
    
    while i <= j:
        x, y = nums[i]**2, nums[j]**2
        
        if x >= y:
            ans[k] = x
            i += 1
        elif y > x:
            ans[k] = y
            j -= 1
        k -= 1
    
    return ans
        
        
        
        
        