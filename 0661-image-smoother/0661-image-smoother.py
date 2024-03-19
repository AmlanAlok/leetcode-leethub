'''
[[1,1,1],[1,0,1],[1,1,1]]
[[100,200,100],[200,50,200],[100,200,100]]
'''
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        return sol(img)

def sol(img):
    
    M, N = len(img), len(img[0])
    
    mat_idx = [(0, 0), 
               (-1, -1), (1, 1), (-1, 1), (1, -1), 
               (0, -1), (0, 1), (1, 0), (-1, 0)]
    
    # How to create a 2D array in python
    ans = [[None]*N for _ in range(M)]
    
    
    def get_filter(m, n):
    
        count = 0
        total = 0

        for p, q in mat_idx:

            if 0 <= m+p < M and 0 <= n+q < N:
                count += 1
                total += img[m+p][n+q]

        flr_avg = total//count
        return flr_avg
    
    
    for m in range(M):
        for n in range(N):
            ans[m][n] = get_filter(m, n)
            
    return ans
            
            
            
            
            
    
    