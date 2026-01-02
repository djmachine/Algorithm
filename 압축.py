def set_dict():
    dic = {}
    
    dic["A"] = 1
    dic["B"] = 2
    dic["C"] = 3
    dic["D"] = 4
    dic["E"] = 5
    dic["F"] = 6
    dic["G"] = 7
    dic["H"] = 8
    dic["I"] = 9
    dic["J"] = 10
    dic["K"] = 11
    dic["L"] = 12
    dic["M"] = 13
    dic["N"] = 14
    dic["O"] = 15
    dic["P"] = 16
    dic["Q"] = 17
    dic["R"] = 18
    dic["S"] = 19
    dic["T"] = 20
    dic["U"] = 21
    dic["V"] = 22
    dic["W"] = 23
    dic["X"] = 24
    dic["Y"] = 25
    dic["Z"] = 26
    
    return dic
        
    

def solution(msg):
    
    dic = set_dict()
    answer = []
    idx = 26
    
    while(msg):
        word = msg[0]
        msg = msg[1:]
        while(msg):
            if word + msg[0] in dic:
                word = word + msg[0]
                msg = msg[1:]
            else:
                break
        
        answer.append(dic[word])
        if msg:
            idx += 1
            dic[word + msg[0]] = idx
    
    return answer

print(solution("TOBEORNOTTOBEORTOBEORNOT"))