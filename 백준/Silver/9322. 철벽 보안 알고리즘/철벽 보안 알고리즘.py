for _ in range(int(input())):
    N = int(input())
    words = {word: i for i, word in enumerate(input().split())}
    Map = {i: words[word] for i, word in enumerate(input().split())}
    
    msg = input().split()
    buf = [None] * N
    for i in range(len(msg)):
        buf[Map[i]] = msg[i]

    print(*buf)