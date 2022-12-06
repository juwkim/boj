input()
prob, duck = 0, 0
while (s:= input())[-1] != '끝':
    if s == '문제':
        prob += 1
    elif prob:
        prob -= 1
    else:
        prob += 2
print('힝구' if prob else '고무오리야 사랑해')