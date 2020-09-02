import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    if check[v]:
        return
    if not check[pre_visit[v]]:
        next_visit[pre_visit[v]] = v
        return
    check[v] = 1
    if next_visit[v]:
        dfs(next_visit[v])
    for i in graph[v]:
        dfs(i)

def solution(n, path, order):
    global graph, check, pre_visit, next_visit
    graph = [[] for _ in range(n)]
    check = [0 for _ in range(n)]
    pre_visit = [0 for _ in range(n)]
    next_visit = [0 for _ in range(n)]
    
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
        
    for a, b in order:
        pre_visit[b] = a
        
    if pre_visit[0]:
        return False
    
    check[0] = 1
    for v in graph[0]:
        dfs(v)
        
    return True if sum(check) == n else False
