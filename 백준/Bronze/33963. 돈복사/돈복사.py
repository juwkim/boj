N = int(S:=input())
cnt = 0
while True:
    N <<= 1
    if len(str(N)) != len(S):
        break
    cnt += 1
print(cnt)