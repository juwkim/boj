n = int(input())
ans, num = [], 1
while n > 0:
    ans.append(num)
    n -= num.bit_count()
    num += 1
if n:
    for i in range(len(ans) - 1, -1, -1):
        if n + ans[i].bit_count() == 0:
            ans.pop(i)
            break
print(len(ans))
print(*ans[::-1])