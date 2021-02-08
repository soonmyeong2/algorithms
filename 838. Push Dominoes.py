class Solution(object):
    def pushDominoes(self, dominoes):
        dominoes = 'L' + dominoes + 'R'
        ans, i = [], 0

        for j in range(1, len(dominoes)):
            if dominoes[j] == '.':
                continue
            if i:
                ans.append(dominoes[i])
            
            bound = j - i - 1
            if dominoes[i] == dominoes[j]:
                ans.append(dominoes[i] * bound)
            elif dominoes[i] == 'L' and dominoes[j] == 'R':
                ans.append('.' * bound)
            elif dominoes[i] == 'R' and dominoes[j] == 'L':
                ans.append('R' * (bound // 2) + '.' * (bound % 2) + 'L' * (bound // 2))
            i = j
        return ''.join(ans)
