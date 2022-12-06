N, A, B, C, D = map(int, input().split())
print(min(-(-N//A)*B, -(-N//C)*D))