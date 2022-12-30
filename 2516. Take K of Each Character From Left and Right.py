class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        limit = {c: s.count(c) - k for c in 'abc'}
        if any(x < 0 for x in limit.values()):
            return -1
        ans = left = 0
        counter = {c: 0 for c in 'abc'}
        for right, c in enumerate(s):
            counter[c] += 1
            while counter[c] > limit[c]:
                counter[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return len(s) - ans
