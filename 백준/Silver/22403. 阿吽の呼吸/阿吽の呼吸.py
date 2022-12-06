cnt = 0
for _ in range(int(input())):
    cnt += 2 * (input() == 'A') - 1
    if cnt < 0:
        break
print('YES' if cnt == 0 else 'NO')