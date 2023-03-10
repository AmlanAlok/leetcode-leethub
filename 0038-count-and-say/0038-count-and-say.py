class Solution:
    def countAndSay(self, n: int) -> str:
        return self.ans1(n)
    
    def ans1(self, n: int) -> str:
        
        cur = '1'
        
        for z in range(n-1):
            i = 0
            j = 0
            count = 0
            t = ''
            while i < len(cur):
                count = 0
                while j < len(cur):

                    if cur[i] == cur[j]:
                        count += 1
                        j += 1
                    else:
                        break
                    
                t += str(count) + cur[i]
                i = j
                
            # print(z, t)
            cur = t
            
        return cur
                
                    
    
    
                
            
        
        
        
    
        
        