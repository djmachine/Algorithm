def solution(prices):
    
    answer = [0 for i in range(len(prices))]

    lis = []
    
    for i in range(len(prices)):
        if lis:
            for j in reversed(lis):
                if prices[i] < j[0]:
                    print(i, prices[i] ,j)
                    answer[j[1]] = i - j[1]
                    lis.remove(j)
        lis.append([prices[i], i])
    
    for i in range(len(answer)):
        if answer[i] == 0:
            answer[i] = len(answer)-1-i 
    
    return answer

print(solution([4,3,3,4,1,2,5,3,4]))