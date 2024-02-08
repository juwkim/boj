from collections import*
cnt = Counter(open(0))
print(1 - sum(V * V for V in cnt.values()) / sum(cnt.values()) ** 2)