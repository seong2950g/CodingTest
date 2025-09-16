answer = [0, 0]

# arr[y1][x1] 부터 arr[y2-1][x2-1] 까지 압축
def compress(y1, x1, y2, x2, arr):
    # 1*1 경우 return
    if y1 == y2:
        answer[arr[y1][x]] += 1
        return
    
    # n*n (n>1) 경우 비교 후 분할 정복
    norm = arr[y1][x1]
    for y in range(y1, y2):
        for x in range(x1, x2):
            if norm != arr[y][x]:
                compress(y1, x1, (y1+y2)//2, (x1+x2)//2, arr)
                compress(y1, (x1+x2)//2, (y1+y2)//2, x2, arr)
                compress((y1+y2)//2, x1, y2, (x1+x2)//2, arr)
                compress((y1+y2)//2, (x1+x2)//2, y2, x2, arr)
                return
            
    answer[norm] += 1
    return
    

def solution(arr):
    y1, x1, = 0, 0
    y2, x2, = len(arr), len(arr[0])
    
    compress(y1, x1, y2, x2, arr)
    
    return answer