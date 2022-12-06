N = int(input())
val = int(input()[-2:])
cnt = 0
for _ in range(N):
    val += int(input()[-2:])
    if val % 100:
        cnt += 1
print(cnt)