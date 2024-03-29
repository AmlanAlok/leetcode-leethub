'''
["KthLargest","add","add","add","add","add"]
[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
["KthLargest","add","add","add","add","add"]
[[1,[]],[-3],[-2],[-4],[0],[4]]
'''

from heapq import heapify, heappush, heappop

class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.heap = nums
#         heapq.heapify(self.heap)        # TC = n
        
#         while len(self.heap) > k:
#             heapq.heappop(self.heap)
        
#     def add(self, val: int) -> int:
#         heapq.heappush(self.heap, val)
#         if len(self.heap) > self.k:
#             heapq.heappop(self.heap)
#         return self.heap[0]
        
    def __init__(self, k:int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        
        while len(self.heap) > self.k:
            heappop(self.heap)
    
    def add(self, val: int):
        heappush(self.heap, val)
        
        if len(self.heap) > self.k:
            heappop(self.heap)
            
        return self.heap[0]
            
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)