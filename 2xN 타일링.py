def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        prev = 2
        answer = 3
        for _ in range(3, n):
            temp = answer
            answer += prev
            prev = temp

    return answer % 1000000007

print(solution(60000))