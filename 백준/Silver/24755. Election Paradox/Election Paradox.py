N = int(input()) + 1
people = sorted(map(int, input().split()))
print(sum(person // 2 for person in people[:N//2]) + sum(people[N//2:]))