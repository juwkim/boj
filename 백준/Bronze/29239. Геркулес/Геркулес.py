def solve():
    while True:
        num = int(input())
        for i in range(1, num + 1):
            print(i)
            s = input()
            if s == "Colder":
                solve()
                input()
            elif s == "Warmer":
                return 0
            else:
                return 1
while True:
    if solve():
        break