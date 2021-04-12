class Solution(object):
    def jump(self, nums):
        left, right, jumps = 0, 0, 0
        
        while right < len(nums) - 1:
            left, right = right + 1, max(i + nums[i] for i in range(left, right + 1))
            jumps += 1
        return jumps
