class Solution(object):
    # O(n) time, O(n) space
    def isPalindrome(self, head):
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
        return nums == nums[::-1]
    
    # O(n) time, O(1) space
    def isPalindrome(self, head):
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
