s = input()
cnt = 0
while len(s) != 1:
    cnt += 1
    s = str(sum(int(i) for i in s))
print(cnt)
if int(s) % 3:
    print('NO')
else:
    print('YES')