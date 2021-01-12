class Solution(object):
    def search(self, nums, target):
        L, R = 0, len(nums)
        
        while L < R:
            M = (L + R) // 2
            
            if target < nums[0] < nums[M]:
                L = M + 1
            elif target >= nums[0] > nums[M]:
                R = M
            elif nums[M] < target:
                L = M + 1
            elif nums[M] > target:
                R = M
            else:
                return M
        return -1
