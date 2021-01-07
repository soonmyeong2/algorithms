#Iterative
class Solution(object):
    def reverseList(self, head):
        prev = None
        
        while head:
            prev, head.next, head = head, prev, head.next
        return prev
    

#Recursive     
class Solution(object):
    def reverseList(self, head, prev=None):
        if head is None:
            return prev
        
        cur, head.next = head.next, prev
        return self.reverseList(cur, head)
