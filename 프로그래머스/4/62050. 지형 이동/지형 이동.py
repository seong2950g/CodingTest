from collections import deque
import heapq

def solution(land, height):
    answer = 0
    n = len(land)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    hq = []
    
    # (0, 0) 부터 탐색 시작
    visited[0][0] = 1
    dq = deque([(0, 0)])
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    
    while dq:
        while dq:
            y, x = dq.popleft()
            curHeight = land[y][x]
            #print(x, y)
            for i in range(len(dx)):
                px, py = x + dx[i], y + dy[i]
                if 0 <= px < n and 0 <= py < n and visited[py][px] == 0:
                    cost = abs(curHeight-land[py][px])
                    if cost > height:
                        heapq.heappush(hq, (cost, y, x, py, px))
                        continue
                    visited[py][px] = 1
                    dq.append((py, px))

        #print(hq)
    
        while hq:
            cost, y, x, py, px = heapq.heappop(hq)
            if visited[y][x] == visited[py][px]:
                continue
                
            #print(cost, px, py)
            answer += cost
            visited[py][px] = 1
            dq.append((py, px))
            break;
            
    return answer