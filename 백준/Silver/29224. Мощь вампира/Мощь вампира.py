n = int(input())
q = ['+'] * n
print(*q, flush=True)
ans = [int(input())]
for i in range(1, n):
    q[i-1], q[i] = '+', '-'
    print(*q, flush=True)
    ans.append((ans[0] - int(input())) // 2)
ans[0] -= sum(ans[1:])
print("answer:", *ans)