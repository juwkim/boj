n = int(input())
vote = [input() for _ in range(n)]
print('S' if max(vote, key=int) == vote[0] else 'N')