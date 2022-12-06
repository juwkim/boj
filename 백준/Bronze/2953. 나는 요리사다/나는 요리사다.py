array = [sum(map(int, input().split())) for _ in range(5)]
print(array.index(max(array))+1, max(array))