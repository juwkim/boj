I = input
R, san, N = int(I()), I(), int(I())
game = [*zip(san, *[I() for _ in [0] * N])]
score = sum(sum((s[0] == s[i]) + 2 * (s[0] + s[i] in 'SP PR RS') for i in range(1, N+1)) for s in game)
IF = sum(max(sum((k == s[i]) + 2 * (k + s[i] in 'SP PR RS') for i in range(1, N+1)) for k in 'SPR') for s in game)
print(score, IF)