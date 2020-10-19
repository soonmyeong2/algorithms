class Solution(object):
    def findRelativeRanks(self, nums):
        sortedNums = sorted(nums, reverse=True)
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i + 1) for i in range(3, len(sortedNums))]
        rankByScore = dict(zip(sortedNums, rank))
        return [rankByScore[num] for num in nums]