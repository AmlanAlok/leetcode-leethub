'''
[1,2,3,4]
[-1,1,0,-3,3]
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return ans2(nums)

'''
TC = n, SC = n
'''
def ans1(nums):
    # print(nums)
    l = len(nums)
    
    ans = [0]*l
    left = [0]*l
    right = [0]*l
    
    left[0] = 1
    
    for i in range(1, l):
        left[i] = left[i-1]*nums[i-1]
    
    right[l-1] = 1
    
    for i in reversed(range(l-1)):
        right[i] = right[i+1] * nums[i+1]
        
    for i in range(l):
        ans[i] = left[i]*right[i]
    
    return ans
    

'''
TC = n, SC = 1
'''
def ans2(nums):
    l = len(nums)
    ans = [0]*l
    
    ans[0] = 1
    
    for i in range(1, l):
        ans[i] = ans[i-1] * nums[i-1]

    r = 1
    
    for i in reversed(range(l)):
        # print(i)
        ans[i] = ans[i] * r
        # print(r, nums[i])
        r = r*nums[i]
    
    return ans
    
    