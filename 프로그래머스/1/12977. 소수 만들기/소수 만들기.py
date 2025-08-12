from itertools import combinations

def solution(nums):
    answer = 0

    for numList in combinations(nums, 3):
        numSum = sum(numList)
        
        for divider in range(2, numSum//2):
            if numSum % divider == 0:
                break;
        else:
            answer += 1
        
    return answer