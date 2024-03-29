'''
[-2,1,-3,4,-1,2,1,-5,4]
[5,4,-1,7,8]
[1]
[1,2]
[-1]
'''
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # return p(nums)
        return prac(nums)    

def dec16(nums):
    ''' Kadane's Algo, TC = n, SC = 1'''
    t = 0
    mx = nums[0]
    
    for n in nums:
        t += n
        
        t = max(t, n)
        mx = max(mx, t)
    
    return mx


def dec17(nums):
    ''' Divide & Conquer, TC = n log(n), SC = log(n)'''
    def helper(nums, left, right):
        
        if left > right:
            return -sys.maxsize
        
        mid = (left + right) // 2
        
        mx_left = 0
        mx_right = 0
        
        cur = 0
        
        for i in range(mid-1, left-1, -1):
            cur += nums[i]
            mx_left = max(mx_left, cur)
        
        cur = 0
        
        for i in range(mid+1, right+1):
            cur += nums[i]
            mx_right = max(mx_right, cur)
            
        mx_total = mx_left + nums[mid] + mx_right
        
        left_half = helper(nums, left, mid-1)
        right_half = helper(nums, mid+1, right)
        
        return max(mx_total, left_half, right_half)
    
    return helper(nums, 0, len(nums)-1)


def p1(self, nums: List[int]) -> int:
    ''' TC = n, SC = 1, ans1 is better solution as it does not use else '''
    maxv = -sys.maxsize
    csum = 0

    for i in nums:

        if i+csum < i:
            csum = i
        else:
            csum += i

        if csum > maxv:
            maxv = csum

    return maxv


def p(nums):
    
    maxi = -sys.maxsize
    t = 0
    
    for n in nums:
        t += n
        
        t = max(t, n)
        maxi = max(maxi, t)
    
    return maxi
        
    
def prac(nums):
    ''' Kadane's Algo, TC = n, SC = 1'''
    largest_sum = -sys.maxsize
    total = 0
    
    for n in nums:
    	
        total += n
        
        if n > total:
        	total = n
        if total > largest_sum:
        	largest_sum = total
    
    return largest_sum
    
    
    

