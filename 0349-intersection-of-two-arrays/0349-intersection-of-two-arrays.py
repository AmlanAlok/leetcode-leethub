class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.ans_2(nums1, nums2)
    
    # TC = O(n+m) average case
    # TC = O(n*m) worst case
    # SC = O(1)
    def ans_2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        print(set(nums1).intersection(set(nums2)))
        return set(nums1).intersection(set(nums2))
    
    def ans_1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        a = set(nums1)
        b = set(nums2)
        
        c = a.intersection(b)
        
#         ans = []
        
#         ans[:] = c
        
#         return ans
        return list(c)