class Solution(object):
    def numDupDigitsAtMostN(self, N):
        def nPr(m, n):
            return 1 if n == 0 else nPr(m, n - 1) * (m - n + 1)
        
        L = list(map(int, str(N + 1)))
        res, n = 0, len(L)

        for i in range(1, n): 
            res += 9 * nPr(9, i - 1)
        used = set()
        for i, x in enumerate(L):
            for y in range(0 if i else 1, x):
                if y not in used:
                    res += nPr(9 - i, n - i - 1)
            if x in used: 
                break
            used.add(x)
        return N - res
