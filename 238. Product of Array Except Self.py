class Solution:
    def productExceptSelf(self, nums):
        ans = [1 for _ in nums]
        left, right = 1, 1
        
        for i in range(len(nums)):
            ans[i] *= left
            ans[~i] *= right
            left *= nums[i]
            right *= nums[~i]
        return ans
