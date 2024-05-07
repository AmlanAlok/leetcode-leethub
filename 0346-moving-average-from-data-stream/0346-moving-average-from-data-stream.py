from collections import deque

class MovingAverage:
    '''
    More efficient ans
    Don't calculate the sum in every invocation
    '''
    def __init__(self, size: int):
        '''SC = n = window size'''
        self.window = deque(maxlen=size)
        self.total = 0
        self.size = size
    
    def next(self, val: int) -> float:
        '''TC = 1'''
        
        if len(self.window) >= self.size:
            first = self.window.popleft()
            self.total = self.total - first + val
        else:
            self.total += val
        
        self.window.append(val)
        
        return self.total/ len(self.window)
        
        
            
        
#     '''
#     Let N = size of window
#     M = number of calls to next
    
#     TC = N*M
#     '''
#     def __init__(self, size: int):
#         self.window = deque(maxlen=size)

#     def next(self, val: int) -> float:
#         self.window.append(val)
        
#         total = 0
        
#         for n in self.window:
#             total += n
        
#         return total/len(self.window)
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


'''
["MovingAverage","next","next","next","next"]
[[3],[1],[10],[3],[5]]
'''
