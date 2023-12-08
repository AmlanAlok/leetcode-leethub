class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return dec07(mat, k)

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
