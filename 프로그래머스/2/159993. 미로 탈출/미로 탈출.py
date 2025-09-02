from collections import deque

def getMinTime(start, end, board):
    m, n = len(board), len(board[0])
    
    visited = [[0 for _ in range(n)] for _ in range(m)]
    dq = deque([start])
    while dq:
        y, x = dq.popleft()
        if (y, x) == end:
            return visited[y][x]
        
        for py, px in [(y, x+1), (y, x-1), (y+1, x), (y-1, x)]:
            if 0 <= py < m and 0 <= px < n and board[py][px] != "X":
                if visited[py][px] == 0 and visited[py][px] < visited[y][x]+1:
                    visited[py][px] = visited[y][x]+1
                    dq.append((py, px))
    
    return -1
        

def solution(maps):
    answer = 0
    
    start, end, lever = 0, 0, 0
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col] == "S":
                start = (row, col)
            elif maps[row][col]  == "E":
                end = (row, col)
            elif maps[row][col]  == "L":
                lever = (row, col)
    
    time1 = getMinTime(start, lever, maps)
    time2 = getMinTime(lever, end, maps)

    if time1 != -1 and time2 != -1:
        return time1 + time2
    else:
        return -1