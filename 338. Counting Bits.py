class Solution(object):
    def countBits(self, num):
        return [bin(i).count('1') for i in range(num + 1)]

    
class Solution(object):
    def countBits(self, num):
        ans = [0]
        for i in range(1, num + 1):
            ans.append(ans[i / 2] + i % 2)
        return ans
