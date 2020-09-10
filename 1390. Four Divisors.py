class Solution:
    def sumFourDivisors(self, nums):
        ans = 0
        
        for num in nums:
            divisor = set() 
            for i in range(1, int(num**.5) + 1):
                if num % i == 0:
                    divisor.update([i, num//i])
                if len(divisor) > 4:    
                    break
            if len(divisor) == 4:
                ans += sum(divisor)
        return ans  