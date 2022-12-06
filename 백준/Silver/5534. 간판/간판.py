g = lambda: [*map(int, input().split())]
N = int(input())
target = input()
l = len(target)
cnt = 0
for _ in range(N):
    s = input()
    for i in range(len(s)-l+1):
        j = 1
        flag = False
        while i + j * (l - 1) < len(s):
            if s[i:i+j*l-j+1:j] == target:
                flag = True
                break
            j += 1
        if flag:
            cnt += 1
            break

print(cnt)