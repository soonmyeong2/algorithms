class Solution(object):
    def lengthOfLongestSubstring(self, s):
        used = dict()
        maxLen = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                maxLen = max(maxLen, i - start + 1)
            used[c] = i
        return maxLen
