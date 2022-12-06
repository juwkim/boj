year = int(input())
print(29 + bool((year % 4 == 0 and year % 100) or year % 400 == 0))