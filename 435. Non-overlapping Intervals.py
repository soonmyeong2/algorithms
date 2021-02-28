class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        check, erased = float('-inf'), 0
        
        for start, end in sorted(intervals, key=lambda (s, e): e):
            if check <= start:
                check = end
            else:
                erased += 1
        return erased
