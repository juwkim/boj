N = int(input())
Min, Max = 1e10, 0
new_Min = 1e10
for num in map(int, input().split()):
    new_Min = min(new_Min, num)
    if num >= Max or (num - new_Min >= Max - Min):
        Min, Max = new_Min, num
    print(Max - Min, end=' ')