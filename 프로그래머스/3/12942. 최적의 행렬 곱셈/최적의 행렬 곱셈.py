INF = 200*200*200*200

def solution(matrix_sizes):
    answer = 0
    
    l = len(matrix_sizes)
    dp = [[INF for _ in range(l)] for _ in range(l)]
    # dp[i][j]는 i번째 행렬부터 j번째 행렬까지의 행렬곱 연산 횟수
    for i in range(l):
        dp[i][i] = 0
    
    # n번의 행렬곱
    for n in range(1, l):
        for i in range(0, l-n):
            for k in range(i, i+n):
                # i번째부터 k번째 행렬을 곱한 행렬의 크기
                left_size = (matrix_sizes[i][0], matrix_sizes[k][1])
                # k+1번째부터 i+n번째 행렬을 곱한 행렬의 크기
                right_size = (matrix_sizes[k+1][0], matrix_sizes[i+n][1])
                cnt = left_size[0]*left_size[1]*right_size[1] + dp[i][k] + dp[k+1][i+n]
                dp[i][i+n] = min(dp[i][i+n], cnt)
                
    return dp[0][l-1]
