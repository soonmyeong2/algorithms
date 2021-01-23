class Solution(object):
    def getIntersectionNode(self, headA, headB):
        p1, p2 = headA, headB
        
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
