from itertools import product

dy = [-1, 0, 0]
dx = [0, -1, 1]
l = 0

def isValid(y, x):
    return 0 <= y < l and 0 <= x < l
    
def solution(clockHands):
    global l
    minRotateCnt = 3 * (8*8) + 1
    l = len(clockHands)
    for firstLine in product([0, 1, 2, 3], repeat=l):
        totalRotateCnt = sum(firstLine)
        rotate = [list(firstLine)]
        nextLine = []
        for y in range(1, l):
            for x in range(l):
                dir = clockHands[y-1][x] + rotate[y-1][x]
                for i in range(3):
                    py = y-1 + dy[i]
                    px = x + dx[i]
                    if isValid(py, px):
                        dir += rotate[py][px]
                        
                rotateCnt = (4 - (dir % 4)) % 4
                nextLine.append(rotateCnt);
                totalRotateCnt += rotateCnt
                
            rotate.append(nextLine)
            nextLine = []
            
        #print(rotate)
        
        #정확성 판단
        for x in range(l):
            dir = clockHands[l-1][x] + rotate[l-1][x]
            for i in range(3):
                py = l-1 + dy[i]
                px = x + dx[i]
                if isValid(py, px):
                    dir += rotate[py][px]
            
            if (dir%4 != 0):
                break
        else:
            minRotateCnt = min(minRotateCnt, totalRotateCnt)
            
    return minRotateCnt