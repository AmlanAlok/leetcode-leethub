class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.p1(matrix)



    '''Approach 1'''
    def p1(self, m: List[List[int]]) -> None:

        r,c = len(m), len(m[0])
        p,q = set(), set()

        for i in range(r):
            for j in range(c):
                if m[i][j] == 0:
                    p.add(i)
                    q.add(j)

        for i in range(r):
            for j in range(c):
                if i in p or j in q:
                    m[i][j] = 0
        



        
    '''Approach 1'''
    def ans1(self, matrix: List[List[int]]) -> None:
        
        r = len(matrix)
        c = len(matrix[0])
        
        rset, cset = set(), set()
        
        for i in range(r):
            for j in range(c):
                
                if matrix[i][j]==0:
                    rset.add(i)
                    cset.add(j)
        
        for i in range(r):
            for j in range(c):
                
                if i in rset or j in cset:
                    matrix[i][j]=0
    
    '''Approach 1'''
    def ans2(self, matrix: List[List[int]]) -> None:
        
        r = len(matrix)
        c = len(matrix[0])
        
        rset, cset = set(), set()
        
        for i in range(r):
            for j in range(c):
                
                if matrix[i][j]==0:
                    rset.add(i)
                    cset.add(j)
        
        for i in rset:
            matrix[i][:] = [0]*c
            
        for j in cset:
            for i in range(r):
                matrix[i][j] = 0

#         for i in range(r):
#             for j in range(c):
                
#                 if i in rset or j in cset:
#                     matrix[i][j]=0
    
    
    '''Approach 2'''
    def fail2(self, matrix: List[List[int]]) -> None:
        
        r=len(matrix)
        c=len(matrix[0])
        
        for i in range(r):
            for j in range(c):
                
                if matrix[i][j]==0:
                    matrix[i][0]='z'
                    matrix[0][j]='z'
                    
        for i in range(r):  
            if matrix[i][0]=='z':
                for j in range(c):
                    matrix[i][j]=0
                    
        for j in range(c):
            if matrix[0][j]==0:
                for i in range(r):
                    matrix[i][j]=0
        
        
    def fail1(self, matrix: List[List[int]]) -> None:
        
        r = len(matrix)
        
        for i in range(r):
            
            c = len(matrix[i])
            
            for j in range(c):
                
                if matrix[i][j]==0:
                    
                    p=0
                    while p<r:
                        matrix[p][j] = 0
                        p+=1
                        
                    q=0
                    while q<c:
                        matrix[i][q] = 0
                        q+=1
                        
                    break
        