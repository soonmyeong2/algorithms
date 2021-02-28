from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        queue, ans = deque(), []

        for i, n in enumerate(nums):
            while queue and nums[queue[-1]] < n:
                queue.pop()
            queue.append(i)
            if k <= i - queue[0]:
                queue.popleft()
            if k <= i + 1:
                ans.append(nums[queue[0]])
        return ans
