from itertools import permutations

def solution(n, weak, dist):
    ans = 101
    weak_point = weak + [weak[i] + n for i in range(len(weak) - 1)]

    for i, start in enumerate(weak):
        for friends in permutations(dist):
            count = 1
            position = start
            for friend in friends:
                position += friend
                if position < weak_point[i + len(weak) - 1]:
                    count += 1
                    position = [w for w in weak_point if w > position][0]
                else:
                    print(friends, count)
                    ans = min(ans, count)
                    break
                    
    return ans if ans != 101 else -1