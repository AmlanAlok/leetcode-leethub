'''
[-2,0,1,3]
2
[3,1,0,-2]
4
[3,2,-2,6,2,-2,6,-2,-4,2,3,0,4,4,1]
3
[]
0
[0]
0
'''
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        return jan5(nums, target)

def jan5(nums, t):
    
    l = len(nums)
    nums.sort()
    c = 0

    for k in range(l-2):
        
        first = nums[k]
        
        i, j = k+1, l-1
            
        while i < j:
            second, third = nums[i], nums[j]
            
            s = first + second + third
            
            if s < t:
                print(first, second, third)
                c += j-i
                i += 1
            else:
                j -= 1
    
    return c
    
def discussion_ans(nums, t):
    nums.sort()
    n = len(nums)
    cnt = 0
    for i in range(n - 2):
        j, k = i + 1, n - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s < t:
                # if (i,j,k) works, then (i,j,k), (i,j,k-1),..., 
                # (i,j,j+1) all work, totally (k-j) triplets
                cnt += k - j
                j += 1
            else:
                k -= 1
    return cnt
        
    

    
    