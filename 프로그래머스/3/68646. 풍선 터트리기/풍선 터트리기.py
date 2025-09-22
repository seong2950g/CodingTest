import heapq

def solution(a):
    answer = 0
    
    # leftMinValue[i] = min(a[:i+1])
    # rightMinValue[i] = min(a[i+1:])
    leftMinValue = [0]*len(a)
    rightMinValue = [0]*len(a)
    
    minHeap = []
    for i in range(len(a)):
        el = a[i]
        heapq.heappush(minHeap, el)
        leftMinValue[i] = minHeap[0]
        
    minHeap = []
    for i in range(len(a)-1, -1, -1):
        el = a[i]
        heapq.heappush(minHeap, el)
        rightMinValue[i] = minHeap[0]
    
    # 최후까지 남길 풍선의 인덱스
    for i in range(len(a)):
        if leftMinValue[i] >= a[i] or rightMinValue[i] >= a[i]:
            answer += 1
    
    return answer