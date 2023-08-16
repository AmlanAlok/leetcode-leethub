import heapq as hq
'''
[1,1,1,2,2,3]
2
[1]
1
[3,0,1,0]
1
'''
"""
The heapq module functions can take either a list of items or a list of tuples as a parameter.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return ans1(nums, k)
    
def ans1(nums, k):
    
    d = {}
    
    for i, v in enumerate(nums):
        if v not in d:
            d[v] = 1
        else:
            d[v] += 1
    
    nums = [(-v, k) for k,v in d.items()]   # -v bcuz we want a max heap
    
    print(nums)
    
    # hq.heapify(nums)
    hq.heapify(nums)
    print(nums)

    ans = []
    for i in range(0, k):
        t = hq.heappop(nums)
        ans.append(t[1])

    return ans
    
        
        