class Solution(object):
    def validMountainArray(self, A):
        peak, valley = 0, 0
        
        for i in range(1, len(A) - 1):
            if A[i - 1] < A[i] > A[i + 1]:
                peak += 1
            if A[i - 1] >= A[i] <= A[i + 1]:
                valley += 1
        return peak == 1 and valley == 0
