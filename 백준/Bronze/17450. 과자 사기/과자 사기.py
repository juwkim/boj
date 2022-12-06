snacks = [list(map(int, input().split())) for _ in range(3)]
gsb = [snack[1]/(10*snack[0] - 500*(snack[0]>=500)) for snack in snacks]
print('SNU'[gsb.index(max(gsb))])