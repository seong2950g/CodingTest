minValue = 25 * 51
trans = {"diamond":0, "iron":1, "stone":2}
DIG = [[1, 1, 1],
      [5, 1, 1],
      [25, 5, 1]]

# idx - minerals에서 처리해야할 idx
def dfs(picks, minerals, idx, accValue):
    global minValue
    # 광석을 모두 캤거나 곡괭이가 없을 경우 종료
    if idx >= len(minerals) or sum(picks) == 0:
        minValue = min(minValue, accValue)
    
    # 다이아 -> 철 -> 돌 순으로 백트래킹
    for i in range(len(picks)):
        # 해당 곡괭이가 남아 있을 경우
        if picks[i] != 0:
            
            picks[i] -= 1 # 해당 곡괭이 사용
            consume = 0 # 해당 곡괭이를 사용하여 소모한 피로도
            
            for j in range(idx, idx+5):
                if j >= len(minerals):
                    break
                nowMineral = trans[minerals[j]]
                consume += DIG[i][nowMineral]
                
            dfs(picks, minerals, j+1, accValue+consume)
            picks[i] += 1 # 되돌리기
            
def solution(picks, minerals):
    
    dfs(picks, minerals, 0, 0)
    
    return minValue