class Solution(object):
    def searchMatrix(self, matrix, target):
        i, j = 0, len(matrix[0]) - 1

        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
                if matrix[i][j] > target:
                    break
            if matrix[i][0] > target:
                break
        return False
