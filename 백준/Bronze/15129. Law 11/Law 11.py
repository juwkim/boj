ballx = int(input().split()[0])

attack = max(int(input().split()[0]) for _ in range(11))
defense = sorted(int(input().split()[0]) for _ in range(11))[-2]
print(+(attack > ballx and attack > 0 and attack > defense))