N, K = map(int, input().split())
sharedCards = sorted(map(int, input().split()))
teamCards = sorted(map(int, input().split()))

left, right = 0, N - 1
top, btm = sharedCards[0], sharedCards[-1]
for _ in range(K):
    leftAns = max(btm * teamCards[left], top * teamCards[left])
    rightAns = max(btm * teamCards[right], top * teamCards[right])
    if leftAns < rightAns:
        right -= 1
    else:
        left += 1

leftAns = max(btm * teamCards[left], top * teamCards[left])
rightAns = max(btm * teamCards[right], top * teamCards[right])
print(max(leftAns, rightAns))