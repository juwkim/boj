for _ in range(int(input())):
    r, e, c = map(int, input().split())
    print('does not matter' if e == r+c else ['do not ', ''][e>r+c] + 'advertise')