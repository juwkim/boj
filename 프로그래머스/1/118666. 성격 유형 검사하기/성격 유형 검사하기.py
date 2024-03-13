def solution(survey, choices):
    dic = {c: 0 for c in "RTCFJMAN"}
    for ((a, b), choice) in zip(survey, choices):
        if choice <= 3:
            dic[a] += 4 - choice
        else:
            dic[b] += choice - 4
    return "".join(max(l, key=dic.get) for l in zip("RCJA", "TFMN"))