class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        return ans(seats)
    
def ans(nums):
    
    N = len(nums)
    dists = []
    
    i = 0
    while i < N and nums[i] != 1:
        i += 1
    dists.append(i)
    
    j = N-1
    while i < j and nums[j] != 1:
        j -= 1
    dists.append(N-j-1)
    
    k = i+1
    while k < j:
        while k < j and nums[k] != 1:
            k += 1
        seats_empty = k-i
        dists.append(seats_empty // 2)
        i = k
        k += 1
        
    print(dists)
    
    return max(dists)
    
    
def ans2(nums):
    
    N = len(nums)
    i = 0
    j = N-1
    
    maxlen = 0
    
    while i < j and nums[i] == 0:
        i += 1
        
    maxlen = max(i + 1, maxlen)
    
    while i < j and nums[j] == 0:
        j -= 1
        
    maxlen = max(N -j +1, maxlen)
    
    
    while i < j:
        c = 0
        
        while i < j and nums[i] == 0:
            i += 1
            c += 1
        maxlen = max(c // 2, maxlen)
        
        c = 0
        
        while i < j and nums[j] == 0:
            j -= 1
            c += 1
        maxlen = max(c // 2, maxlen)
        
        i += 1
    
    return maxlen

'''
[1,0,0,0,1,0,1]
[1,0,0,0]
[0,1]
[1,0,0,1]
[0,0,1]
'''
            
        
    