'''
[2,7,4,1,8,1]
[1]
[7,5,8]
'''
from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        return ans1(stones)

'''TC = n, SC = n'''
def ans1(stones):
    
    nums = [i*-1 for i in stones]
    heapify(nums)
    # heapq._heapify_max(stones)        # allows you to create a max heap but I do not know it corresponding functions yet
    # print(nums)
    

    while len(nums) >= 2:
        # y, x = nums[0]*-1, nums[1]*-1           # fails here [7,5,8]
        
        y = heappop(nums) * -1
        x = heappop(nums) * -1
        
        if x != y:
            y = y-x
            heappush(nums, y*-1)
    
        # print(nums)
    
    return nums[0]*-1 if len(nums) == 1 else 0
    
    