'''
Testcases

[[0,1,2,0],
[3,4,5,2],
[1,3,1,5]]

[[1,1,1],
[1,0,1],
[1,1,1]]

[[1,2,3,4],
[5,0,7,8],
[0,10,11,12],
[13,14,15,0]]
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.p2(matrix)
        
        
    '''Approach 2'''
    def p3(self, m: List[List[int]]) -> None:

        r, c = len(m), len(m[0])
        
        row_z, col_z = False, False
        
        for i in range(r):
            if m[i][0] == 0:
                row_z = True
                break
        
        for j in range(c):
            if m[0][j] == 0:
                col_z = True
                break
        
        for i in range(1, r):
            for j in range(1, c):
                v = m[i][j]
                if v == 0:
                    m[i][0] = 0
                    m[0][j] = 0
        
        for i in range(1, r):
            if m[i][0] == 0:
                for j in range(c):
                    m[i][j] = 0
        
        for j in range(1, c):
            if m[0][j] == 0:
                for i in range(r):
                    m[i][j] = 0

        if row_z:
            for i in range(r):
                m[i][0] = 0

        if col_z:
            for j in range(c):
                m[0][j] = 0
        
    '''Approach 2'''
    def p2(self, m: List[List[int]]) -> None:

        r, c = len(m), len(m[0])
        
        row_z, col_z = False, False
        
        i = 0
        while i < r:
            if m[i][0] == 0:
                row_z = True
            i+=1
        
        j = 0
        while j < c:
            if m[0][j] == 0:
                col_z = True
            j+=1
        
        i = 1
        while i < r:
            j = 1
            while j < c:
                v = m[i][j]
                if v == 0:
                    m[i][0] = 0
                    m[0][j] = 0
                j+=1
            i+=1
        
        print(m)
        
        for i in range(1, r):
            if m[i][0] == 0:
                for j in range(c):
                    m[i][j] = 0
        
        for j in range(1, c):
            if m[0][j] == 0:
                for i in range(r):
                    m[i][j] = 0

        if row_z:
            for i in range(r):
                m[i][0] = 0

        if col_z:
            for j in range(c):
                m[0][j] = 0
        


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
        