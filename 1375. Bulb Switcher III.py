class Solution(object):
    def numTimesAllBlue(self, light):
        ans, cnt = 0, 0

        for i, l in enumerate(light, 1):
            cnt += i
            cnt -= l
            if cnt == 0:
                ans += 1
                
        return ans