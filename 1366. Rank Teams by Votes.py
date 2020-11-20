class Solution(object):
    def rankTeams(self, votes):
        rank = {char: [0] * len(votes[0]) + [char] for char in votes[0]}
        for vote in votes:
            for i, vote in enumerate(vote):
                rank[vote][i] -= 1
        return ''.join(sorted(votes[0], key=rank.get))
