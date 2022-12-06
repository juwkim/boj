a, b = map(int, input().split())
print(abs((a-1)//4 - (b-1)//4) + abs((a-1)%4 - (b-1)%4))