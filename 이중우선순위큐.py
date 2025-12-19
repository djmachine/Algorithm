def solution(operations):
    
    answer = []
    
    for i in operations:
        order = i.split(" ")
        if order[0] == "I":
            answer.append(int(order[1]))
        elif order[0] == "D" and answer:
            if order[1] == "1":
                answer.remove(max(answer))
            elif order[1] == "-1":
                answer.remove(min(answer))
    
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0,0]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))