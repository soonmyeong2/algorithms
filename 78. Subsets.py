class Solution(object):
    def subsets(self, nums):
        ans = []
        for i in range(len(nums) + 1):
            ans.append([list(c) for c in combinations(nums, i)])
        return sum(ans, [])