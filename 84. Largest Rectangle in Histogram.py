class Solution(object):
    def largestRectangleArea(self, heights):
        stack, ans = [], 0
        
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i if not stack else i-stack[-1]-1
                ans = max(ans, height * width)
            stack.append(i)
        return ans
