T = int(input())
for _ in range(T):
    R, S = input().split()
    words = []
    for Alphabet in S:
        for _ in range(int(R)):
            words.append(Alphabet)
    print("".join(words))
    