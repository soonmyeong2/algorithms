class Solution():
    def rob(self, nums):
        cur = pre = 0
        for num in nums:
            pre, cur = cur, max(i+pre cur)
        return cur
