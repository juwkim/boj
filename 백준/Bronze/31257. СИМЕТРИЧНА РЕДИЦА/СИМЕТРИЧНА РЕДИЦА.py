N = int(input())
S = input()
for i in range(N):
    if S[i:] == S[i:][::-1]:
        print(i)
        if i:
            print(S[:i][::-1])
        break