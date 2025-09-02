numToStr = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 
    6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 
    12: 'C', 13: 'D', 14: 'E', 15: 'F'
}

def getNBasedNum(decimal, n):
    num = ''
    if decimal == 0:
        return '0'
    
    while decimal > 0:
        decimal, mod = divmod(decimal, n)
        num += numToStr[mod]
        
    return num[::-1]


def solution(n, t, m, p):
    answer = ''

    numList = [] #숫자를 한글자씩 차례대로 저장
    nowDecimal = 0
    # 0부터 숫자를 1씩 늘려가며 n진수로 변환하고 한글자씩 numList에 추가
    while len(numList) < t*m:
        nBasedNum = getNBasedNum(nowDecimal, n)
        for el in nBasedNum:
            numList.append(el)
            
        nowDecimal += 1
    
    nowIdx = p-1
    for _ in range(t):
        answer += numList[nowIdx]
        nowIdx += m
    
    return answer