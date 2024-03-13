'''
[1,2,1]
[0,1,2,2]
[1,2,3,2,2]
[3,3,3,1,2,1,1,2,3,3,4]
[0,1,2,3,4,5,6,7]
'''

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        return p9(fruits)
    
def ans1(nums: List[int]) -> int:
    
    d = {}
    i=j=0
    m=0
    l = len(nums)
    
    while j<l:
        
        while j<l and len(d.items()) <= 2:
            n = nums[j]
            
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
            
            mlen = (j-i+1)
            
            if m < mlen and len(d.items()) <= 2:
                m = mlen
                
            j+=1
        
        while i<l and len(d.items()) > 2:
            
            n = nums[i]
            
            d[n]-=1
            
            if d[n] == 0:
                del d[n]
                
            i+=1
    
    return m

def dec20(nums):
    ''' TC = n, SC = k+1 where k is the maximum window size '''
    j = 0
    d = {}
    mx = 0
    l = len(nums)
    
    for j in range(l):
        n = nums[j]
        
        d[n] = d.get(n, 0) + 1
        
        if len(d) <= 2:
            mx += 1
        else:
            i = j - mx
            m = nums[i]
            d[m] -= 1
            if d[m] == 0:
                del d[m]
    return mx

def error_dec20(nums):
    '''TC = n log(n), SC = n'''
    '''Incorrect Understanding'''
    d = {}
    s = []
    
    for n in nums:
        d[n] = d.get(n, 0) + 1
        
    for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True):
        s.append(v)
        if len(s) == 2:
            print(s)
            return sum(s)
        
    return s[0]
        
def p9(fruits):
    '''TC = n, SC = k+1'''
    l = len(fruits)
    d = {}
    i = 0
    mx = 0
    
    for j in range(l):
        
        n = fruits[j]
        
        d[n] = d.get(n, 0) + 1
        
        if len(d) <= 2:
            mx += 1
        else:
            i = j - mx
            z = fruits[i]
            d[z] -= 1
            if d[z] == 0:
                del d[z]
    
    return mx

# def p(fruits):
    
    

    
    
            
    