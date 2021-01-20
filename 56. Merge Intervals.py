class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        out = []

        for i in intervals:
            if out and i[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out += i,
        return out
