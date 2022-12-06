while W:= int(input()):
    wife = [input() for _ in range(W)]
    husband = [input() for _ in range(int(input()))]
    wife.extend(husband)
    
    wife.sort(key=lambda x: (-ord(x[0]), x[1]))
    print(*wife)