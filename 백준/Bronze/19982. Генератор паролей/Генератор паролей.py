n = int(input())
a, b, _ = map(int, input().split())
g = lambda x, y, z: [chr(x + (i - x) % z) for i in range(x, x + y)] 
print(''.join(g(65, a, 26) + g(97, b, 26) + g(48, n - a - b, 10)))