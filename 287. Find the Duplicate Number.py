# O(n) time and O(n) space
from collections import defaultdict
class Solution(object):
    def findDuplicate(self, nums):
        n = defaultdict(int)
        for num in nums:
            if n[num]:
                return num
            n[num] += 1
            
            
# O(nlogn) time and O(1) space
class Solution(object):
    def findDuplicate(self, nums):
        left, right = 1, len(nums)-1
        while left < right:
            mid = (right + left)/2
            if sum(i <= mid for i in nums) > mid:
                right = mid
            else:
                left = mid+1
        return right
    
    
# O(n) time and O(1) space    
class Solution:
    def findDuplicate(self, nums):
        t, h = nums[0], nums[nums[0]]
        while t != h:
            t, h = nums[t], nums[nums[h]]
        t = 0
        while t != h:
            t, h = nums[t], nums[h]
        return t
    
    
# O(n) time and O(1) space 
class Solution(object):
	def findDuplicate(self, nums):
		for index in range(len(nums)):
			i = abs(nums[index])
			if nums[i] > 0:
				nums[i] = -(nums[i])
			else:
				return i