def toList(s):
    answer = []
    stack = []
    temp = []
    num = ""
    
    for i in s:
        if i == "{":
            stack.append(i)
        elif i == ",":
            if len(stack) == 2:
                temp.append(int(num))
                num = ""
        elif i == "}":
            if len(stack) == 1:
                stack.pop()
            else:
                temp.append(int(num))
                answer.append(temp)
                num = ""
                temp = []
                stack.pop()
        else:
            num += i
    
    return answer

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    
    return arr

def solution(s):
    temp = []
    answer = []
    pr = toList(s)

    for i in range(len(pr)-1):
        for j in range(i+1, len(pr)):
            if len(pr[j]) == i+1:
                pr = swap(pr,i,j)
    
    for i in pr:
        for j in i:
            if j not in answer:
                answer.append(j)
        
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))