class Solution:
    def countAndSay(self, n: int) -> str:
        return self.ans3(n)
    
    '''3 loops'''
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
    
    '''Recursion with 2 loops'''
    def ans2(self, n: int) -> str:
        
        if n == 1:
            return '1'
        
        x = self.ans2(n-1)
        
        i, j = 0, 0
        t = ''
        while i < len(x):
            count = 0
            while j < len(x):
                if x[i] == x[j]:
                    count += 1
                    j += 1
                else:
                    break
            t += str(count) + x[i]
            i = j
        
        return t
    
    '''24 ms ans from solution'''
    def ans3(self, n: int) -> str:
        
        def say(s: str) -> str:
            s = s + "#"
            c, res = 1, ""
            for i in range(1, len(s)):
                if s[i] != s[i-1]:
                    # Output
                    res += str(c)+s[i-1]
                    c = 1
                else:
                    c += 1
            return res

        res = "1"
        for i in range(1, n):
            res = say(res)
        
        return res
    
    
                
            
        
        
        
    
        
        