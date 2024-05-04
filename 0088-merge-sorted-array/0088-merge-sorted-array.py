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
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        return may04_24(nums1, m, nums2, n)
    

def ans1(nums1, m, nums2, n):
    ''' TC = m+n, SC = m '''
    
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
    
    # return nums1


def ans2(nums1, m, nums2, n):
    ''' TC = m+n, SC = 1 '''
    
    i = m+n-1           # last index
    j, k = m-1, n-1
    
    while i>=0:     # TC = m+n
        
        if k<0 or (j>=0 and nums1[j] >= nums2[k]):
            nums1[i] = nums1[j]
            j-=1
        # elif j<0 or (k>=0 and nums2[k] > nums1[j]):
        #     nums1[i] = nums2[k]
        #     k-=1
        else:
            nums1[i] = nums2[k]
            k-=1
        
        i-=1
    
    # return nums1
    

def may04_24(nums1, m, nums2, n):
    '''TC = m+n, SC = 1'''
    k = len(nums1)-1
    i = m-1
    j = n-1
    
    while k >= 0:
        
        if j < 0 or (i >= 0.and nums1[i] >= nums2[j]):
            nums1[k] = nums1[i]
            i -= 1
        elif i < 0 or (j >= 0 and nums1[i] < nums2[j]):
            nums1[k] = nums2[j]
            j -= 1
        
        k -= 1
    
    
    
def may03_24(nums1, m, nums2, n):
    '''TC = m+n, SC = 1'''
    
    i = m-1
    j = n-1
    k = len(nums1)-1
    
    while k >= 0:
        
        if i >= 0 and j >= 0 and nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        elif i >= 0 and j >= 0 and nums1[i] < nums2[j]: 
            nums1[k] = nums2[j]
            j -= 1
        elif i == -1:
            while j >= 0:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        elif j == -1:
            while i >= 0:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            
        k -= 1
    
        