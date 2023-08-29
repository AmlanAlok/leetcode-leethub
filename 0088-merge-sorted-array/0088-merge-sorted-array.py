'''
[1,2,3,0,0,0]
3
[2,5,6]
3
[1]
1
[]
0
[0]
0
[1]
1
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        return ans1(nums1, m, nums2, n)
    
'''
TC = m+n, SC = m
'''
def ans1(nums1, m, nums2, n):
    
    a = nums1[:m]       # SC = m
    
    i,j,k = 0,0,0
    
    while k < m+n:      # TC = m+n
        
        if j>=n or (i<m and a[i] <= nums2[j]):
            nums1[k] = a[i]
            i+=1
        else:
            nums1[k] = nums2[j]
            j+=1
        k+=1
    
    return nums1
        