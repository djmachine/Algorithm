def solution(skill, skill_trees):
    
    answer = 0
    
    for skill_tree in skill_trees:
        
        now_skill = ""
        
        for tree in skill_tree:
            if tree in skill:
                now_skill += tree
        
        if skill[:len(now_skill)] == now_skill:
            answer += 1
    
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))