class Solution(object):
    def canPartition(self, nums):
        if sum(nums) % 2 == 0:
            target = sum(nums) // 2 
            cur = set({0})
            for i in nums:
                cur.update({i + x for x in cur})
                if target in cur:
                    return True
        return False
    
    
class Solution(object):
    def canPartition(self, nums):
        if len(nums) == 1:
            return False
        
        stack, visit = [(0, 0, 0)], set((0, 0, 0))
        while stack:
            x, y, i = stack.pop()
            if i == len(nums) and x == y:
                return True
            if i < len(nums) and (x+nums[i], y, i+1) not in visit:
                stack.append((x+nums[i], y, i+1))
                visit.add((x+nums[i], y, i+1))
            if i < len(nums) and (x, y+nums[i], i+1) not in visit:
                stack.append((x, y+nums[i], i+1))
                visit.add((x, y+nums[i], i+1))
        return False