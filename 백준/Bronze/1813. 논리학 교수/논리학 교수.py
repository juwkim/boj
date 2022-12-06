from collections import Counter
input()
talk = sorted(Counter(map(int, input().split())).items(), reverse=True)
flag = 0
for a,b in talk:
    if a == b:
        flag = a
        break
print(flag if flag or talk[-1][0] else -1)