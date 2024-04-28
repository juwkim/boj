def solution(clothes):
    dic = {}
    for cloth_name, cloth_type in clothes:
        dic[cloth_type] = dic.get(cloth_type, 1) + 1
    answer = 1
    for v in dic.values():
        answer *= v
    answer -= 1
    return answer