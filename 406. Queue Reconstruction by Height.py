class Solution(object):
    def reconstructQueue(self, people):
        reco = []
        
        people.sort(key=lambda (h, k): (-h, k))
        for p in people:
            reco.insert(p[1], p)
        return reco
