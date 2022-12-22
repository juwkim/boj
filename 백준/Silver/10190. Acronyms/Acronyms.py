for _ in range(int(input())):
    S, N = input().split()
    print(S)
    for _ in range(int(N)):
        line = input()
        word = ''.join([i[0] for i in line.split()])
        if S == word:
            print(line)