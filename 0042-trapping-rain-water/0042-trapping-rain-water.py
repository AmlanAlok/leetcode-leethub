'''
[0,1,0,2,1,0,1,3,2,1,2,1]
[4,2,0,3,2,5]
[4,2,3]
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        return dec06(height)
    
    ''' Two pointer, TC = n, SC = 1 '''
    def ans1(self, h: List[int]) -> int:
        
        i, j = 0, len(h)-1
        left_max, right_max = 0, 0
        
        ans = 0
        
        while i<j:
            
            p, q = h[i], h[j]
            
            if p < q:
                if p >= left_max:
                    left_max = p
                else:
                    ans += left_max - p
                
                i+=1
            else:
                if q >= right_max:
                    right_max = q
                else:
                    ans += right_max - q
                
                j-=1
                
        return ans
    
    def fail1(self, h: List[int]) -> int:
        
        i = 0
        l = len(h)
        
        for k in range(l):
            if h[k] > 0:
                i = k
                break
        
        j, t, w = i, 0, 0
        
        while i < l and j < l:
            
            p, q = h[i], h[j]
            
            if p > q:
                t += p-q
                if j == l-1 and t != 0:
                    i += 1
                    j = i
                    t = 0
                # else:
                    # j+=1
            elif p <= q:
                i = j
                w += t
                t = 0
            
            j+=1
            
            # elif j == l-1 and t != 0:
            #     i += 1
            #     j = i
            #     t = 0
            
            # if p == q:
            #     j+=1
            
        w += t
        
        return w
    
    '''
    My answer
    I was making the mistake of clubbing all the water within two high points ans then updating it when ching the max points
    
    Two pointer, TC = n, SC = 1 '''
    def ans2(self, h: List[int]) -> int:
        
        i, j = 0, len(h)-1
        left_max, right_max = 0, 0
        
        lt, rt, w = 0, 0, 0
        
        while i<j:
            
            p, q = h[i], h[j]
            
            if q > right_max:
                # w += rt
                # rt = 0
                right_max = q
            
            if q < right_max:
                w += right_max - q
                
            if p > left_max:
                # w += lt
                # lt = 0
                left_max = p
                
            if p < left_max:
                w += left_max - p
            
            if p >= q:
                j-=1
            
            if p < q:
                i+=1
        
        return w
    
def dec06(height):
    
    left_max, right_max = 0, 0
    w = 0
    i, j = 0, len(height)-1
    
    while i < j:
        
        p, q = height[i], height[j]
        
        if p > left_max:
            left_max = p
        if p < left_max:
            w += (left_max - p)
        
        if q > right_max:
            right_max = q
        if q < right_max:
            w += (right_max - q)
            
        if p >= q:
            j -= 1
        if p < q:
            i += 1
    
    return w
    
    
    
                    
                
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
                
        