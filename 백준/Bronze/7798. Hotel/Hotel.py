g = lambda: [*map(int, input().split())]

for i in range(1, 1 + int(input())):
    N, M = g()
    hotel = []
    for _ in range(N):    
        *l, name = input().split()
        # bad_size, room_capa, room_num, price, name
        hotel.append([*map(int, l)] + [name])
    team = []
    for _ in range(M):
        bad_size_type, *l = input().split()
        team.append([bad_size_type] + [*map(int, l)])
        
        # bad_size_type, people_num, max_person
    print(f'Case #{i}:')
    i += 1
    for bad_size_type, people_num, max_person in team:
        temp = []
        for bad_size, room_capa, room_num, price, name in hotel:
            if {'A': 20, 'B': 36, 'C': 49}[bad_size_type] <= bad_size <= {'A': 35, 'B': 48, 'C': 62}[bad_size_type]:
                a = min(max_person, room_capa)
                required_room = (people_num + a - 1) // a
                if room_num >= required_room:
                    temp.append([required_room * price, bad_size, name])
        if temp:
            s = min(temp, key=lambda x: (x[0], -x[1], temp.index(x)))
            print(s[0], s[2])
        else:
            print('no-hotel')