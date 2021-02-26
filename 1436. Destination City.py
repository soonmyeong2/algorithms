class Solution(object):
    def destCity(self, paths):
        A, B = map(set, zip(*paths))
        return (B - A).pop()
