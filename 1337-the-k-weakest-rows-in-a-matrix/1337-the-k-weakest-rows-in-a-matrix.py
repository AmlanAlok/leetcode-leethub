'''
[[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
2
[[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
1
'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return dec08(mat, k)

''' TC = m*n+ m*log(m), SC = m'''
def dec07(mat, k):
    
    t = []      # SC = m
    
    for i in range(len(mat)):       # n^2
        nums = mat[i]
        count = 0
        for n in nums:
            if n == 1:
                count += 1
        t.append((count, i))
    
    print(t)
    t.sort()        # n log n
                 
    ans = []
    for (k, v) in t[:k]:
        ans.append(v)
    
    return ans

''' TC = m*n, SC = 1 '''
def dec08(mat, k):
    
    l, b = len(mat), len(mat[0])
    ans = []
    
    for j in range(b):
        for i in range(l):
        
            n = mat[i][j]
            
            if n == 0:
                if j == 0 or mat[i][j-1] == 1:
                    ans.append(i)
                    
                    if len(ans) == k:
                        print(k)
                        return ans
    p = 0
    while len(ans) < k and p < l:
        if mat[p][-1] == 1:
            ans.append(p)
        p += 1
        
    return ans
         
