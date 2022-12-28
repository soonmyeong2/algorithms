class Solution(object):
    def lenLongestFibSubseq(self, A):
        s = set(A)
        dp = collections.defaultdict(lambda: 2)
        for j in range(len(A)):
            for i in range(j):
                if A[j] - A[i] < A[i] and A[j] - A[i] in s:
                    dp[A[i], A[j]] = dp[(A[j] - A[i], A[i])] + 1
        return max(dp.values() or [0])

