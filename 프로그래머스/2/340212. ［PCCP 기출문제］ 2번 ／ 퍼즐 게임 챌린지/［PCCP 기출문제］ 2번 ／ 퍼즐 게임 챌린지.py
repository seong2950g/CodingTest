# diffs, times, limit, level을 바탕으로 퍼즐이 해결가능한지 판단
def isSolve(diffs, times, limit, level):
    totalTime = 0
    
    timePrev = times[0]
    for i in range(1, len(diffs)):
        diff, timeCur = diffs[i], times[i]
        if diff <= level:
            totalTime += timeCur
        else:
            nFailed = diff - level
            perTime = timeCur + timePrev
            totalTime += (perTime * nFailed) + timeCur
                
        timePrev = timeCur
        if totalTime > limit:
            return False
    
    return True

def solution(diffs, times, limit):
    answer = 0
    
    diffs.insert(0, 0)
    times.insert(0, 0)
    
    # 해결가능한 숙련도를 이진탐색
    lo, hi = 0, 300001
    level = (lo + hi) // 2
    while lo+1 < hi:
        if isSolve(diffs, times, limit, level):
            hi = level
        else:
            lo = level
            
        level = (lo + hi) // 2

    return hi
