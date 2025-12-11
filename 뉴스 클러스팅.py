def toDict(st):
    st_dict = {}
    
    for i in range(len(st)-1):
        if st[i].isalpha() and st[i+1].isalpha():
            n_str = (st[i]+st[i+1]).upper()

            if n_str not in st_dict:
                st_dict[n_str] = 1
            else:
                st_dict[n_str] += 1
    
    return st_dict

def solution(str1, str2):
    
    str1_dict = toDict(str1)
    str2_dict = toDict(str2)
    dif = {}
    uni = {}
    dif_num = 0
    uni_num = 0
    
    str1_lis = [i for i in str1_dict]
    str2_lis = [i for i in str2_dict]

    for i in str1_lis:
        if i in str2_lis:
            dif[i] = min(str1_dict[i], str2_dict[i])
            uni[i] = max(str1_dict[i], str2_dict[i])
        else:
            uni[i] = str1_dict[i]
    
    for i in str2_lis:
        if i in str1_lis:
            dif[i] = min(str1_dict[i], str2_dict[i])
            uni[i] = max(str1_dict[i], str2_dict[i])
        else:
            uni[i] = str2_dict[i]
    
    for i in dif.values():
        dif_num += i
        
    for i in uni.values():
        uni_num += i
        
    if dif_num == 0 and uni_num == 0:
        return 65536
    else:
        return ((dif_num/uni_num) * 65536) // 1
    
print(solution("FRANCE", "french"))