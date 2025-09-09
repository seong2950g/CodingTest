# 플로이드 워셜 알고리즘 
def solution(n, s, a, b, fares):
    answer = 201 * 100000
    
    INF = 201 * 100000
    # 최단 경로 저장 배열
    f = [[INF for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        f[i][i] = 0
        
    for c, d, fare in fares:
        f[c][d] = fare
        f[d][c] = fare
        
    for k in range(1, n+1):
        for y in range(1, n+1):
            for x in range(1, n+1):
                f[y][x] = min(f[y][x], f[y][k]+f[k][x])
                
    # S지점에서 i지점까지 합승, i지점에서 각자 도착지점까지 계산
    for i in range(1, n+1):
        total = f[s][i] + f[i][a] + f[i][b]
        answer = min(answer, total)
    
    # 합승하지 않고 S지점에서 각자 도착지점까지 계산
    total = f[s][a] + f[s][b]
    answer = min(answer, total)
    
    return answer