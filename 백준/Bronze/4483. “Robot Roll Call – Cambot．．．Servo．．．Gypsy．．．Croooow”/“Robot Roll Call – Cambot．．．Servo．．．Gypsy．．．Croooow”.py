for i in range(1, 1 + int(input())):
    names = {input(): 0 for _ in range(int(input()))}
    for _ in range(int(input())):
        for check in input().split():
            try:
                names[check]
                names[check] = 1
            except:
                pass
    
    print(f"Test set {i}:")
    for name, i in names.items():
        print(f'{name} is {["absent", "present"][i]}')
    print()