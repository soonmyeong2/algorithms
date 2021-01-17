class Solution(object):
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = []
        
        for i, temperature in enumerate(T):
            while stack and T[stack[-1]] < temperature:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
        return ans
