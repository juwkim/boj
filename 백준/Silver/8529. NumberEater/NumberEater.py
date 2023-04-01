n = int(input())
a = [int(input()) for i in range(n)]

unique_meals = {}

for i in range(n):
    for j in range(i, n):
        meal_hash = hash(tuple(sorted(set(a[i:j+1]))))
        if meal_hash in unique_meals:
            unique_meals[meal_hash] += 1
        else:
            unique_meals[meal_hash] = 1

print(len(unique_meals))