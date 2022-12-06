while (n := int(input())):
    deck = [input() for _ in range(n)]
    for i, j in zip(range(n//2), range(n//2 + n%2, n)):
        print(deck[i], deck[j], sep='\n')
    if n % 2:
        print(deck[n//2])