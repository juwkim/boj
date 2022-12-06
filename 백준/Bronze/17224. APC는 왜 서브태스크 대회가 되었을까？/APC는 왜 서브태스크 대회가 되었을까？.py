N, L, K = map(int, input().split())

score = 0
under_L = 0
for _ in range(N):
    sub1, sub2 = map(int, input().split())
    
    if K and sub2 <= L:
        score += 140
        K -= 1
    else:
        under_L += (sub1 <= L)

score += 100 * min(K, under_L)
print(score)