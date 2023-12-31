'''
7
[2,3,1,2,4,3]
4
[1,4,4]
11
[1,1,1,1,1,1,1,1]
11
[1,2,3,4,5]
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        return dec31(target, nums)
    
def dec31(target, nums):
    
    l = len(nums)
    mini = sys.maxsize
    total = 0
    
    i = 0
    j = 0
    
    while j < l:
        
        while total < target and j < l:
            total += nums[j]
            j += 1
        
        while total >= target and i < l:
            mini = min(mini, j-i)
            total -= nums[i]
            i += 1
            
    return 0 if mini == sys.maxsize else mini
          
def ans1(target: int, nums: List[int]) -> int:
    ''' Two Pointer/ Sliding Window, TC = n, SC = 1 '''
    
    m = sys.maxsize
    i = j = s = 0
    l = len(nums)
    
    while j < l:
        
        while s < target and j < l:
            s+=nums[j]
            j+=1
        
        while s >= target and i < l:
            if m > (j-i):
                m = j-i
            s-=nums[i]
            i+=1
        
    return 0 if m == sys.maxsize else m

def ans2(target: int, nums: List[int]) -> int:
    
    total = left = right = 0
    res = len(nums) + 1

    while right < len(nums):
        total += nums[right]
        while total >= target:
            res = min(res, right-left+1)
            total -= nums[left]
            left += 1
        right += 1
    return res if res <= len(nums) else 0 

def dec18(target, nums):
    ''' Two Pointer/ Sliding Window, TC = n, SC = 1 '''
    
    l = len(nums)
    i = j = 0
    s = 0
    mini = sys.maxsize
    
    while j < l:
        
        while s < target and j < l:
            s += nums[j]
            j += 1
            
        while s >= target and  i < l:
            mini = min(mini, j-i)   # there is no +1 bcuz j's value of 1 greater than the position we are looking for
            s -= nums[i]
            i += 1
            
    return 0 if mini == sys.maxsize else mini
    
        
        
    
    
        
        

    
    