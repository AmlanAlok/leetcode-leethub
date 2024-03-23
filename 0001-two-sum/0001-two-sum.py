'''
[2,7,11,15]
9
[1,2,3,7,3]
6
[3,3]
6
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return sol(nums, target)
    
def dec22(nums, t):
    d = {}
    
    for i in range(len(nums)):
        n = nums[i]
        
        v = t - n
        
        if v in d:
            return [d[v], i]
        else:
            d[n] = i
    
    return []
    
def y22aug01(self, nums: List[int], target: int) -> List[int]:

    dict = {v:i for i,v in enumerate(nums)}

    for i in range(len(nums)):

        c = target-nums[i]
        if c in dict and i is not dict[c]:
            return [i, dict[c]]

    return False
        
def y22aug02(self, nums: List[int], target: int) -> List[int]:
    ''' TC = n, SC = n '''
    d = {}

    for i,v in enumerate(nums):

        c= target-v

        if c in d and d[c] != i:
            return [i, d[c] ]
        else:
            d[v] = i

    return []

        
''' != not required'''    
def old_p5(self, nums: List[int], t: int) -> List[int]:

    d = {}

    for i in range(len(nums)):

        v = nums[i]
        c = t - v

        if c in d and i != d[c]:
            return [d[c], i]
        else:
            d[v] = i
        
def sol(nums, target):
    
    d = {}
    
    for i in range(len(nums)):
        
        n = nums[i]
        diff = target - n
        
        if diff in d:
            return [d[diff], i]
        else:
            d[n] = i
        
    return []
        
