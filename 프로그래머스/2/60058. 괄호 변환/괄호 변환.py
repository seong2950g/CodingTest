def isCorrect(u):
    stack = []
    
    for el in u:
        if el == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        else:
            stack.append(el)
    
    if len(stack) == 0:
        return True
    return False
                

def rec(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열 반환
    if len(p) == 0:
        return ''
    
    # 2. 두 "균형잡힌 괄호 문자열" u, v로 분리
    left, right = 0, 0 # 좌,우 괄호의 개수
    u, v = p, ''
    for i in range(len(p)):
        if p[i] == "(":
            left += 1
        else:
            right += 1
        
        # 더 이상 분리할 수 없는 가장 작은 균형잡힌 문자열 u
        if left == right:
            u = p[:i+1]
            v = p[i+1:]
            break
            
    print(u, v)
    
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면
    if isCorrect(u):
        # 3-1. 문자열 v에 대해 1단계 부터 다시 수행하고, 수행한 결과 문자열을 u에 이어 붙힌 후 반환
        return u + rec(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면
    else:
        reverse = ''
        for el in u[1:-1]:
            if el == '(':
                reverse += ')'
            else:
                reverse += '('
                
        return '(' + rec(v) + ')' + reverse
    

def solution(p):
    answer = rec(p)
    
    return answer