from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.window = deque(maxlen=size)

    def next(self, val: int) -> float:
        self.window.append(val)
        
        total = 0
        
        for n in self.window:
            total += n
        
        return total/len(self.window)
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
