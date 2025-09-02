import heapq
from collections import deque

INF = 101**2

def solution(n, costs):
    minCost = 0
    
    minHeap = []
    weights = [[INF for _ in range(n)] for _ in range(n)]
    for x, y, cost in costs:
        weights[x][y] = cost
        weights[y][x] = cost
    
    visited = [False] * n
    
    # 0번 노드부터 
    visited[0] = True
    for i, cost in enumerate(weights[0]):
        # 0번 노드와 연결된 모든 노드를 cost 기준 minHeap에 넣음
        if cost != INF:
            heapq.heappush(minHeap, (cost, 0, i))
    
    # n-1개의 간선을 찾으면 완료
    for _ in range(n-1):
        cost, x, y = heapq.heappop(minHeap)
        
        # 방문하지 않은 노드를 찾을 때까지 minHeap에서 꺼내기
        while visited[y]:
            cost, x, y = heapq.heappop(minHeap)
        
        minCost += cost
        
        # 방문하지 않은 노드 방문 처리
        visited[y] = True
        for i, cost in enumerate(weights[y]):
            # 연결된 모든 노드를 cost 기준 minHeap에 넣음
            if cost != INF:
                heapq.heappush(minHeap, (cost, y, i))       
        
    return minCost