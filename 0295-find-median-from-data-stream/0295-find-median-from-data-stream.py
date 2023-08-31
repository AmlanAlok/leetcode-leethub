'''
heapq.heappushpop(heap, item)
    Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop()
'''


import heapq as hp

class MedianFinder:

    def __init__(self):
        self.minh = []  # the larger half of the list, min heap
        self.maxh = []  # the smaller half of the list, max heap
        
    def addNum(self, num: int) -> None:
        if len(self.minh) == len(self.maxh):
            heappush(self.minh, -heappushpop(self.maxh, -num))
        else:
            heappush(self.maxh, -heappushpop(self.minh, num))

    def findMedian(self) -> float:
        if len(self.minh) == len(self.maxh):
            return float(self.minh[0] - self.maxh[0]) / 2.0
        else:
            return float(self.minh[0])
        
        
    ''' This one is slower'''
#     def __init__(self):
#         self.maxh = []
#         self.minh = []

#     def addNum(self, num: int) -> None:
#         hp.heappush(self.maxh, -num)
#         hp.heappush(self.minh, -hp.heappop(self.maxh))
        
#         if len(self.minh) > len(self.maxh):
#             hp.heappush(self.maxh, -hp.heappop(self.minh))
        
#     def findMedian(self) -> float:
        
#         if len(self.maxh) > len(self.minh):
#             return -self.maxh[0]
#         else:
#             return (self.minh[0] + (-self.maxh[0]))/2

    
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()