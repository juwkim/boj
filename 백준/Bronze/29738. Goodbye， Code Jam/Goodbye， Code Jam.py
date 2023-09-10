for tc in range(1, 1 + int(input())):
    N = int(input())
    if N > 4500:
        y = "Round 1"
    elif N > 1000:
        y = "Round 2"
    elif N > 25:
        y = "Round 3"
    else:
        y = "World Finals"
    print(f"Case #{tc}: {y}")