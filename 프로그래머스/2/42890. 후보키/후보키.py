from itertools import combinations

def solution(relation):
    candiIdx = set()
    
    for n in range(1, len(relation[0])):
        for selectIdx in combinations(range(0, len(relation[0])), n):
            
            # 현재 선택된 인덱스들에 대해 최소성이 아닌 경우 제외
            passFlag = False
            for x in range(1, len(selectIdx)):
                for partIdx in combinations(selectIdx, x):
                    if partIdx in candiIdx:
                        passFlag = True
                        break
                if passFlag: break
            if passFlag: continue
                    
            checkSet = set()
            for record in relation:
                tmp = []
                for i in selectIdx:
                    tmp.append(record[i])
                checkSet.add(tuple(tmp))
                
            if len(checkSet) == len(relation):
                candiIdx.add(selectIdx)
    
    if len(candiIdx) == 0:
        return 1
    else:
        return len(candiIdx)
    
    