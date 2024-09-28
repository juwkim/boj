for _ in range(int(input())):
    N = int(input())
    print(("NIE", "TAK")[N % 9 == 0 or N % 3 == 2])