from collections import Counter


class Solution(object):
    # without most_common method
    def topKFrequent(self, nums, k):
        frq = defaultdict(int)
        
        for key, cnt in Counter(nums).items():
            frq[key] = cnt
        return [key for key, cnt in sorted(frq.items(), key=lambda x: -x[1])][:k]
    
    # with most_common method    
    def topKFrequent(self, nums, k):
        return [item for item, count in Counter(nums).most_common(k)]
