cards = sum([input().split() for _ in range(4)], [])
flag = False
for i in range(10):
    for j in range(i+1, 11):
        for k in range(j+1, 12):
            a, b, c = cards[i], cards[j], cards[k]
            if all(len(set(i)) in [1, 3] for i in zip(a, b, c)):
                print(i+1, j+1, k+1)
                flag = True
if not flag:
    print('no sets')