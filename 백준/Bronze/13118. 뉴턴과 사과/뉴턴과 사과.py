people = input().split()
apple = input().split()[0]
try:
    print(people.index(apple) + 1)
except:
    print(0)