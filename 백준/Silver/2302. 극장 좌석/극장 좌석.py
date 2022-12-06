fibo = [1, 1, 2]
for i in range(38):
    fibo.append(fibo[-2] + fibo[-1])
N = int(input())
ans, prev = 1, 0
for _ in range(int(input())):
    cur = int(input())
    ans *= fibo[cur - prev - 1]
    prev = cur
ans *= fibo[N - prev]
print(ans)