from collections import defaultdict


class Solution(object):
    def findTargetSumWays(self, nums, S):
        count = defaultdict(int)
        count[0] = 1
    
        for num in nums:
            step = defaultdict(int)
            for i in count:
                step[i + num] += count[i]
                step[i - num] += count[i]
            count = step
        return count[S]
