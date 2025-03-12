import sys
input = lambda: sys.stdin.readline().rstrip()

while (s:=input())[0] != 'E':
    N = int(s.split()[1])
    dealer = sum(map(lambda x: int(x, 2), input().split()))
    player = 255 + max(int(x, 2) for x in input().split())
    bytes = [int(x, 2) for x in input().split()[::-1]]
    nibbles = [int(x, 2) for x in input().split()[::-1]]
    input()
    print(f"HAND {N}")
    for _ in range(4):
        if dealer >= 510 or dealer >= player:
            break
        if dealer < 382:
            dealer += bytes.pop()
            print("Byte me!")
        elif dealer <= 500:
            dealer += nibbles.pop()
            print("Nibble me!")
    if dealer > 510:
        print("Bust!")
    elif dealer >= player:
        print("Win!")
    else:
        print("Lose!")