class Solution(object):
    def checkValidString(self, s):
        left = right = 0
        
        for i in range(len(s)):
            left += -1 if s[i]  == ')' else 1
            right += -1 if s[~i] == '(' else 1
            if left < 0 or right < 0: 
                return False
        return True
