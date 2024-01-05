'''
[-1,2,1,-4]
1
[0,0,0]
1
[4,0,5,-5,3,3,0,-4,-5]
-2
[1,1,1,0]
-100
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        return jan5(nums, target)
    
def ans1(nums, t):
    
    n = len(nums)
    nums.sort()
    k = 0
    m = sys.maxsize
    closest_sum = sys.maxsize
    prev_k = nums[0]-1
    
    while k < n-2:
        
        if nums[k] == prev_k:
            k+=1
            continue
        
        i = k+1
        j = n-1
        
        while i < j:
            
            s = nums[k] + nums[i] + nums[j]
            
            diff = abs(t-s)
            if diff < m:
                m = diff
                closest_sum = s
                
            if s > t:       # I was comparing with 0
                j-=1
            elif s < t:     # I was comparing with 0
                i+=1
            else:
                return s
            
        prev_k = nums[k]
        k+=1
    
    return closest_sum
    
def jan5(nums, t):
    '''TC = n2, SC = n (worst) or 1 (best)'''
    l = len(nums)
    nums.sort()
    mn = sys.maxsize
    last_val = None
    closest_sum = sys.maxsize
    
    for k in range(l-2):
        
        first = nums[k]
        
        if first == last_val:
            continue
        
        i = k+1
        j = l-1
        
        while i < j:
            second, third = nums[i], nums[j]
            
            s = first + second + third
            
            if s == t:
                return s
            diff = abs(s - t)
            if  diff < mn:
                mn = diff
                closest_sum = s
                
            if s < t:
                i += 1
            elif s > t:
                j -= 1

        last_val = first
    
    return closest_sum
                
                
        
    