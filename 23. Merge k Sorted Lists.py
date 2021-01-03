import heapq


class Solution(object):
    def mergeKLists(self, lists):
        heap = list()
        head = tail = ListNode()

        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
        while heap:
            tail.next = ListNode(heapq.heappop(heap))
            tail = tail.next
        return head.next
