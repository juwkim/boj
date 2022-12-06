P, K = map(int, input().split())

key = 0
if P%2 == 0: key = 2*(K>2)
elif P%3 == 0: key = 3*(K>3)
else:
    i = 5
    while i <= min(int(P**.5), K):
        if P%i == 0:
            key = i
            break
        elif P%(i+2) == 0:
            key = i+2
            break
        i += 6
print(f'BAD {key}' if key and key < K else 'GOOD')