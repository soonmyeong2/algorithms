class Solution(object):
    def isPalindrome(self, s):
        s = [e.lower() for e in s if e.isalnum()]
        return s == s[::-1]
