class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = tail = ListNode()
        
        while l1 and l2:
            if l1.val<=l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2
        return head.next