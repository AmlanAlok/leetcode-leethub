'''
[2,3,-2,4]
[2,-5,3,1,-4,0,-10,2,8]
[-2,0,-1]
[-4,-3,-2]
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return p1(nums)

def failed_attempt(nums: List[int]) -> int:
        
        m = -sys.maxsize
        a = 1
        zf = True
        
        for i in range(len(nums)):
            
            n = nums[i]
            if n == 0 and zf:
                a = 1
                continue
            
            zf = False
            a *= n
            
            # if a < n:
            #     a = n
            if m < a:
                m = a
        
        if m == -sys.maxsize:
            m = 0
        return m
    
def ans1(nums: List[int]) -> int:
        
    amax, amin = nums[0], nums[0]
    ans = amax

    t = math.prod(nums)

    if t > 0:
        return t

    for i in range(1, len(nums)):

        n = nums[i]

        new_max = amax*n
        new_min = amin*n

        amax = max(n, new_max, new_min)
        amin = min(n, new_max, new_min)

        ans = max(ans, amax)

    return ans
            
def p1(nums):
    ans = nums[0]
    mx = nums[0]
    mn = nums[0]
    
    t = math.prod(nums)
    if t > 0:
        return t
    
    for i in range(1, len(nums)):
        n = nums[i]
        
        new_mx, new_mn = mx*n, mn*n
        
        mx = max(n, new_mx, new_mn)
        mn = min(n, new_mx, new_mn)

        ans = max(ans, mx)
    
    return ans

