class Solution(object):
    def majorityElement(self, nums):
        used = dict()
        for num in nums:
            if num not in used:
                used[num] = 1
            else:
                used[num] += 1
        return sorted(used.items(), key=lambda x: x[1])[-1][0]