import bisect


class Solution(object):
    def searchRange(self, nums, target):
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        return [left, right - 1] if left < right else [-1, -1]
