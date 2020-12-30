class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        ans = n = ListNode()
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, mod = carry // 10, carry % 10
            n.next = ListNode(mod)
            n = n.next
        return ans.next
