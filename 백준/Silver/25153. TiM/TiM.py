N = int(input())
M = int(input())

x_cnt = 0
total_digit = 0
total_num = 0

ans = 0
num = 0
cmd = '+'
for _ in range(M):
    c = input()
    if c == 'X':
        x_cnt += [-1, 1][cmd == '+']
    elif c in '+-':
        ans += [-1, 1][cmd == '+'] * num
        total_num += num
        num = 0
        cmd = c
    else:
        c = int(c)
        total_digit += c
        num = num * 10 + c
ans += [-1, 1][cmd == '+'] * num
total_num += num

print(total_digit)
print(total_num)
print(-ans // x_cnt)