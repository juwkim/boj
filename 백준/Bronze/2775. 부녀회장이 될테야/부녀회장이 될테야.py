T = int(input())
# 15 x 15 사이즈의 리스트 생성
residents = [[num for num in range(15)]] + [[0 for col in range(15)] for row in range(14)]
max_floor, max_room = 1, 0

for _ in range(T):
    floor, room = int(input()), int(input())
    if residents[floor][room]:
        print(residents[floor][room])
    else:
        for x in range(max_room + 1, room + 1):
            for y in range(1, max_floor + 1):
                residents[y][x] = sum(residents[y - 1][:x + 1])
        for x in range(room + 1):
            for y in range(max_floor, floor + 1):
                residents[y][x] = sum(residents[y - 1][:x + 1])    
        max_floor, max_room = floor, room
        print(residents[floor][room])