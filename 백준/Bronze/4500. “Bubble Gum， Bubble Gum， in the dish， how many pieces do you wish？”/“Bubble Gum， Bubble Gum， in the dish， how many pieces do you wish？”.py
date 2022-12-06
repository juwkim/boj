for _ in range(int(input())):
    a = input().split()
    print(a[(a.index(input()) + int(input()) - 1)%len(a)])