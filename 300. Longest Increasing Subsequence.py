class Solution(object):
    # O(nlogn) time
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        

    # O(nlogn) time
    def lengthOfLIS(self, nums):
        dp = []
        
        for num in nums:
            idx = bisect.bisect_left(dp, num)
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num
        return len(dp)
