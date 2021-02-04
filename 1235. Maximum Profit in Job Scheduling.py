class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        schedule = sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)])
        earn = 0
        heap = []
        
        for start, end, profit in schedule:
            while heap and heap[0][0] <= start:
                _, gain = heapq.heappop(heap)                
                earn = max(earn, gain)
            heapq.heappush(heap, (end, earn + profit))
        while heap:
            _, gain = heapq.heappop(heap)                
            earn = max(earn, gain)
        return earn
