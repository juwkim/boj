a = ((-3, 0.0625), (-1, 0.125), (0, 0.375),
     (1, 0.25), (2, 0.125), (3, 0.0625))

dic = {i:0 for i in range(-60, 61)}
check = dict(a)

print('Round   A wins    B wins    Tie')
print('    1   43.7500%  18.7500%  37.5000%')
for s in range(2, 21):
    for key in check:
        if check[key]:
            for m, n in a:
                dic[key + m] += check[key] * n
    check = dic.copy()
    dic = {i:0 for i in range(-60, 61)}

    A, B, T = 0, 0, 0
    for i, j in check.items():
        if i > 0: A += j
        elif i < 0: B += j
        else: T += j
    print(f'{s:#5d}{A*100:#10.4f}%{B*100:#9.4f}%{T*100:#9.4f}%')