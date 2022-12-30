class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        dist = [min(abs(startIndex - i), len(words) - abs(startIndex - i)) for i, x in enumerate(words) if x == target]
        return min(dist or [-1])
