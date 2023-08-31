import heapq as hp

class MedianFinder:

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

    def __init__(self):
        self.small = []  # the larger half of the list, min heap
        self.large = []  # the smaller half of the list, max heap
        
    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.small, -heappushpop(self.large, -num))
        else:
            heappush(self.large, -heappushpop(self.small, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.small[0] - self.large[0]) / 2.0
        else:
            return float(self.small[0])
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()