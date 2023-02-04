facs = [1]
for i in range(1, 10):
    facs.append(facs[-1] * i)

ans = []
num = int(input())
idx = 9
while num:
    if facs[idx] <= num:
        ans.append(idx)
        num -= facs[idx]
    else:
        idx -= 1
if ans == [1]:
    print(0)
else:
    print(*ans[::-1], sep="")