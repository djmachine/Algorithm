def solution(triangle):
    
    answer = []
    
    for i in triangle:
        if len(i) == 1:
            answer = i
        else:
            new_answer = []
            for j in range(len(i)):
                if j == 0:
                    new_answer.append(answer[j] + i[j])
                else:
                    if j < len(answer):
                        left = answer[j-1] + i[j]
                        right = answer[j] + i[j]
                        new_answer.append(max(left, right))
                    else:
                        new_answer.append(answer[j-1]+i[j])
            answer = new_answer
    
    return max(answer)

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))