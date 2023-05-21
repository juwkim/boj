N, A, B = map(int, input().split())

if A == B and B >= N:
    print('Anything')
elif A < B or B < N:
    print('Bus')
else:
    print('Subway')