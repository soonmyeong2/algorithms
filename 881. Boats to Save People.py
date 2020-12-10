from collections import deque

class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort(reverse=True)
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit: j -= 1
            i += 1
        return i
    
        '''
        people = deque(sorted(people))
        count = 0    
        while people:
            boat = people.pop()
            if people and boat + people[-1] <= limit:
                boat += people.pop()
            elif people and boat + people[0] <= limit:
                boat += people.popleft()
            count += 1
        return count
        '''