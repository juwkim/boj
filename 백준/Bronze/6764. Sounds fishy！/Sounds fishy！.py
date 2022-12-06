A = [int(input()) for _ in range(4)]
if len(set(A)) == 1:
    print('Fish At Constant Depth')
elif len(set(A)) != 4:
    print('No Fish')
elif A == sorted(A):
    print('Fish Rising')
elif A == sorted(A, reverse=True):
    print('Fish Diving')