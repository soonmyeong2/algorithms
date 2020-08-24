class Solution(object):
    def hammingWeight(self, n):
        return len([i for i in range(32) if (1<<i)&n])