def solution(m, n, puddles):
    answer = [[0] * (m+1) for _ in range(n+1)]
    answer[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j,i] in puddles:
                continue
            elif j == 1 and i == 1:
                continue
            else:
                answer[i][j] = (answer[i-1][j] + answer[i][j-1]) % 1000000007

    return answer[n][m] 

print(solution(4,3,	[[2, 2]]))