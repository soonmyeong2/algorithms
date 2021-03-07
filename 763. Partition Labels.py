class Solution(object):
    def partitionLabels(self, S):
        ans = []
        
        while S:
            i = 1
            while set(S[:i]) & set(S[i:]):
                i += 1    
            ans.append(i)
            S = S[i:]
        return ans
    
    def partitionLabels2(self, S):
        last = {char: i for i, char in enumerate(S)}
        left, right = 0, 0
        ans = []

        for i, char in enumerate(S):
            right = max(right, last[char])
            if i == right:
                ans.append(right - left + 1)
                left = i + 1
        return ans
