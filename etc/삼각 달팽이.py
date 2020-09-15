def solution(n):
    ans = [[0]*(i+1) for i in range(n)]
    N, p, d, c = n, 0, 0, 1
    
    while N:
        for i in range(N):
            if d == 0:
                ans[i+2*p][p] = c
            elif d == 1:
                ans[n-p-1][i+p+1] = c
            elif d == 2:
                ans[N-i+2*p][-p-1] = c                
            c += 1
        p += 1 if d == 2 else 0
        d = (d+1)%3 
        N -= 1
        
    return sum(ans, [])
