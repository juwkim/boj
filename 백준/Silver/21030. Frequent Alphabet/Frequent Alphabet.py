N = int(input())
cnt = [0] * 26
for a, b in zip(input(), input()):
    cnt[ord(a) - 97] += 1
    if a != b:
        cnt[ord(b) - 97] += 1
print(max(cnt))