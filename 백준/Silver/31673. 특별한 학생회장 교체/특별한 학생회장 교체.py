N, M, *V = map(int, open(0).read().split())
Sum = sum(V)
vote, cnt = 0, 1
for num in sorted(V, reverse=True):
    vote += num
    cnt += 1
    if vote * 2 >= Sum:
        break
print(M // cnt)