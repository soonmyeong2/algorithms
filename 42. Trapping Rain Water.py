class Solution(object):
    def trap(self, height):
        ans = 0
        maxValue = max(height) if len(height) != 0 else -1
        high = [i for i, h in enumerate(height) if maxValue == h]
        if len(high) == 0: return 0
    
        cur = height[0]
        for i in range(1, high[0]):
            if cur > height[i]:
                ans += cur - height[i]
            cur = max(height[i], cur)
            
        cur = height[-1]
        for i in range(len(height)-2, high[-1], -1):
            if cur > height[i]:
                ans += cur - height[i]
            cur = max(height[i], cur)
            
        for i in range(high[0], high[-1]):
            if height[high[0]] > height[i]:
                ans += height[high[0]] - height[i]
                
        return ans
                
