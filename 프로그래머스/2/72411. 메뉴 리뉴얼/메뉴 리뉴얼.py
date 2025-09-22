from itertools import combinations

def solution(orders, course):
    answer = []
    
    # comb[n]을 사용하여 n개의 주문 조합을 저장할 딕셔너리
    # comb[3]이면, 3가지의 주문조합을 저장하는 딕셔너리
    comb = [dict() for _ in range(11)]
    
    for order in orders:
        for i in course:
            for el in combinations(order, i):
                # 사전 순으로 오름차순 정렬
                el = sorted(list(el))
                el = ''.join(el)
                if el in comb[i]:
                    comb[i][el] += 1
                else:
                    comb[i][el] = 1
                
    for dic in comb:
        if len(dic) == 0:
            continue
            
        # 가장 많이 주문된 횟수 찾기
        maxCnt = 0
        for el, cnt in dic.items():
            if cnt > maxCnt:
                maxCnt = cnt
                
        if maxCnt < 2:
            continue
        
        # 가장 많이 주문된 조합 찾기
        for el, cnt in dic.items():
            if cnt == maxCnt:
                answer.append("".join(el))
        
    return sorted(answer)