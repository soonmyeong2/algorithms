from collections import deque

def solution(board):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    ans = float('inf')
    n = len(board)
    queue = deque()
    queue.append((0, 0, -1, 0))
    visit = {(0, 0, 0) : 0, (0, 0, 1) : 0, (0, 0, 2) : 0, (0, 0, 3) : 0}

    while queue:
        x, y, d, cost = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                newcost = cost
                if d == -1:
                    newcost += 100
                elif (d - i) % 2 == 0:
                    newcost += 100
                else:
                    newcost += 600
                if nx == n - 1 and ny == n - 1:
                    ans = min(ans, newcost)
                elif (nx, ny, i) not in visit or visit.get((nx, ny, i)) > newcost:
                    visit[(nx, ny, i)] = newcost
                    queue.append((nx, ny, i, newcost))
    return ans
