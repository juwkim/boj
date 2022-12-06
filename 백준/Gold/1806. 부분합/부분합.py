N, S = map(int, input().split())
seq = [*map(int, input().split())]
left, right, ans = 0, 0, 100000
check = seq[left]
while True:
    if check >= S:
        ans = min(ans, right - left + 1)
        check -= seq[left]
        left += 1
    else:
        right += 1
        if right == N:
            break
        check += seq[right]
print(ans if ans != 100000 else 0)