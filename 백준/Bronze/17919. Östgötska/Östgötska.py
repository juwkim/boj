s = input().split()
if sum('ae' in i for i in s) >= 0.4 * len(s):
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')