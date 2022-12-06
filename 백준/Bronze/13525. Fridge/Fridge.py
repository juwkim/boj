cnt = [0] * 10
for i in input():
    cnt[int(i)] += 1

num = 1
for i in range(10):
    if cnt[i] < cnt[num]:
        num = i
if num:
    print(str(num) * (cnt[num] + 1))
else:
    print('1' + str(num) * (cnt[num] + 1))