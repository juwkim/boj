channels = [input() for _ in range(int(input()))]
kbs1, kbs2 = channels.index('KBS1'), channels.index('KBS2')
kbs2 += (kbs2 < kbs1)
print('1' * kbs1 + '4' * kbs1 + '1' * kbs2 + '4' * (kbs2 - 1))