C = list(input())

for _ in range(int(input())):
    tmp = [[], []]
    for idx, card in enumerate(C[::-1]):
        tmp[idx&1].append(card)
    C = tmp[1] + tmp[0]
print(*C, sep='')