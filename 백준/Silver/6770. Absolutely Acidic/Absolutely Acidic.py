from collections import Counter

cnt = Counter(int(input()) for _ in range(int(input())))
l = cnt.most_common()
if l[0][1] == l[1][1]:
    Min, Max = l[0][0], l[0][0]
    for i in range(1, len(l)):
        if l[0][1] != l[i][1]:
            continue
        Min = min(Min, l[i][0])
        Max = max(Max, l[i][0])
    print(Max - Min)
else:
    num = l[0][0]
    Min, Max = l[1][0], l[1][0]
    for i in range(2, len(l)):
        if l[1][1] != l[i][1]:
            continue
        Min = min(Min, l[i][0])
        Max = max(Max, l[i][0])
    print(max(abs(num - Max), abs(num - Min)))    