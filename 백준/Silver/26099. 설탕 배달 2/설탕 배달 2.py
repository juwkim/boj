N = int(input())
if N == 4 or N == 7:
    print(-1)
else:
    five, left = divmod(N, 5)
    if left == 0:
        print(five)
    elif left == 1:
        print(five + 1)
    elif left == 2:
        print(five + 2)
    elif left == 3:
        print(five + 1)
    elif left == 4:
        print(five + 2)