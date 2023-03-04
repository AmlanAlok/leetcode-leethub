class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return self.p4(numRows)
    
        
    def ans1(self, numRows: int) -> List[List[int]]:
        
        ans = []
        
        for i in range(1,numRows+1):
            
            if i == 1:
                ans.append([1])
            if i == 2:
                ans.append([1, 1])
            if i > 2:
                a = [1]
                for j in range(i-2):
                    a.append(ans[i-2][j] + ans[i-2][j+1])
                a.append(1)
                ans.append(a)
        
        print(ans)
        return ans
        
    def ans2(self, numRows: int) -> List[List[int]]:
        
        n = numRows
        a = []
        
        i=1
        
        while i<=n:
            
            if i==1:
                a.append([1])
            if i==2:
                a.append([1,1])
            if i>2:
                x = [None]*i
                x[0], x[-1] = 1, 1

                j=1

                while j<(len(x)-1):
                    x[j] = a[i-2][j] + a[i-2][j-1]
                    j+=1

                a.append(x)
            
            i+=1
        
        return a
        
    def p2(self, numRows: int) -> List[List[int]]:
        
        n=numRows
        a=[]
        
        if n>=1:
            a.append([1])
        if n>=2:
            a.append([1,1])
        
        if n>2:
            # print(a)
            k=3
            while k<=n: 
                b = [None]*k
                b[0], b[k-1] = 1, 1

                for i in range(1,k-1):
                    b[i] = a[k-2][i]+ a[k-2][i-1]

                a.append(b)
                k+=1
        
        return a
        
    '''This code is not good'''
    def p3(self, numRows: int) -> List[List[int]]:
        
        n = numRows
        ans = []
        
        for i in range(n):
            
            a = []
            
            if i == 0:
                a.append(1)
            if i == 1:
                a = [1, 1]
            elif i>1:
                a.append(1)
                for j in range(1, i):
                    a.append(ans[i-1][j] + ans[i-1][j-1])
                
                a.append(1)
                    
            ans.append(a)
            
        return ans
            
    def p4(self, numRows: int) -> List[List[int]]:
        
        n = numRows
        a = []
        
        if n>=1:
            a.append([1])
        if n>=2:
            a.append([1,1])
        if n>2:
            for i in range(3,n+1):
                b = [None]*i
                b[0], b[len(b)-1] = 1, 1
                
                for j in range(1, len(b)-1):
                    # (i-1) is wrong and I have made this mistake multiple times
                    # b[j] = a[i-1][j] + a[i-1][j-1]        
                    b[j] = a[i-2][j] + a[i-2][j-1]
                
                a.append(b)
                
        return a
    
    def p5(self, numRows: int) -> List[List[int]]:
        
        n = numRows
        ans = []
        
        if n >= 1:
            ans.append([1])
        if n >= 2:
            ans.append([1,1])
            
        i = 2
        while i < n:
            temp = [None]*(i+1)
            temp[0], temp[-1] = 1, 1
            
            j = 1
            while j < (len(temp)-1):
                temp[j] = ans[i-1][j] + ans[i-1][j-1]
            
            ans.append(temp)
        
        return ans
            
        
        
        
        
        