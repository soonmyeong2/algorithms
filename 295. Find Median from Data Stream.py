from heapq import *


class MedianFinder(object):
    
    def __init__(self):
        self.heaps = [], []
        
        
    def addNum(self, num):
        low, high = self.heaps
        heappush(high, -heappushpop(low, -num))
        if len(low) < len(high):
            heappush(low, -heappop(high))
            
            
    def findMedian(self):
        low, high = self.heaps
        if len(low) > len(high):
            return -low[0]
        else:
            return (high[0] - low[0]) / 2.0
