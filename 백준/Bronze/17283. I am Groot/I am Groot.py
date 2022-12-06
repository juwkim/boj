L = int(input())
R = int(input()) / 100
total_len = 0
branch_num = 2
while True:
    L = int(L * R)
    if L <= 5:
        break
    total_len += L * branch_num
    branch_num *= 2
print(total_len)