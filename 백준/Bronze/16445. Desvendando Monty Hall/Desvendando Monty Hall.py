n = int(input())    
print(n - [input() for _ in range(n)].count('1'))