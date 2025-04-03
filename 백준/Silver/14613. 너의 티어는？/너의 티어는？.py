from math import comb

W, L, D = map(float, input().split())
ans = [0] * 5
for win in range(21):
    for lose in range(21 - win):
        draw = 20 - win - lose
        ans[(win - lose) // 10 + 2] += comb(20, win) * comb(20 - win, lose) * W**win * L**lose * D**draw
for i in range(5):
    print(f"{ans[i]:.8f}")