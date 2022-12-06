L, R, A = map(int, input().split())
R, L = sorted([R, L])
print([2*(R+A), 2*L + (-L+R+A)//2*2][L < R + A])