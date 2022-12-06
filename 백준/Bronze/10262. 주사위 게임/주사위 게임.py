g = lambda: sum(map(int, input().split()))
a, b = g(), g()
print('Gunnar' if a > b else 'Emma' if a < b else 'Tie')