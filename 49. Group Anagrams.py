from collections import defaultdict


class Solution(object):
    # Use sort
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        
        for word in strs:
            groups[tuple(sorted(word))].append(word)
        return groups.values()
    
    # Not use sort
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        
        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - 97] += 1
            groups[''.join(map(lambda x: x.rjust(2, '-'), map(str, key)))].append(word)
        return groups.values()
