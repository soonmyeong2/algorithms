from collections import deque

def getValidPosition(p1, p2, board):
    pos = []
    
    for p in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        if board[p1[0] + p[0]][p1[1] + p[1]] == 0 and board[p2[0] + p[0]][p2[1] + p[1]] == 0:
            pos.append({(p1[0] + p[0], p1[1] + p[1]),(p2[0] + p[0], p2[1] + p[1])})
    
    if p1[0] == p2[0]:
        for i in [-1, 1]:
            if board[p1[0] + i][p1[1]] == 0 and board[p2[0] + i][p2[1]] == 0:
                pos.append({(p1[0] + i, p1[1]),(p1[0], p1[1])})
                pos.append({(p2[0] + i, p2[1]),(p2[0], p2[1])})
    else:
        for i in [-1, 1]:
            if board[p1[0]][p1[1] + i] == 0 and board[p2[0]][p2[1] + i] == 0:
                pos.append({(p1[0], p1[1]),(p1[0], p1[1] + i)})
                pos.append({(p2[0], p2[1]),(p2[0], p2[1] + i)})
    return pos
    
def solution(board):
    ans = float('inf')
    queue = deque()
    queue.append([{(1, 1), (1, 2)}, 0])
    visit = {frozenset({(1, 1), (1, 2)}) : 0}
    
    newBoard = [[1 for _ in range(len(board) + 2)] for _ in range(len(board) + 2)]
    for i in range(len(board)):
        for j in range(len(board)):
            newBoard[i+1][j+1] = board[i][j]
            
    while queue:
        position, cost = queue.popleft()
        position = list(position)
        cost += 1
        
        for p in getValidPosition(position[0], position[1], newBoard):
            p = frozenset(p)
            if (len(board), len(board)) in p:
                ans = min(ans, cost)
            elif p not in visit or visit.get(p) > cost:
                visit[p] = cost
                queue.append([p, cost])
    return ans
