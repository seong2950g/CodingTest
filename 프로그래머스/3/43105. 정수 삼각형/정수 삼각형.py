def solution(triangle):
    
    for lineIdx in range(1, len(triangle)):
        for elIdx in range(lineIdx+1):
            # 삼각형의 가장 왼쪽 숫자인 경우
            if elIdx == 0:
                triangle[lineIdx][elIdx] += triangle[lineIdx-1][elIdx]
            # 삼각형의 가장 오른쪽 숫자인 경우
            elif elIdx == len(triangle[lineIdx])-1:
                triangle[lineIdx][-1] += triangle[lineIdx-1][-1]
            else:
                candi1 = triangle[lineIdx-1][elIdx-1]
                candi2 = triangle[lineIdx-1][elIdx]
                maxValue = max(candi1, candi2)
                triangle[lineIdx][elIdx] += maxValue
    
    return max(triangle[-1])