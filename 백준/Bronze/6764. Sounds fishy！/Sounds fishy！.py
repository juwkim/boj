A = [int(input()) for _ in range(4)]
if len(set(A)) == 1:
    print('Fish At Constant Depth')
else:
    if all(a < b for a, b in zip(A, A[1:])):
        print('Fish Rising')
    elif all(a > b for a, b in zip(A, A[1:])):
        print('Fish Diving')
    else:
        print('No Fish')