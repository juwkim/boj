for _ in range(int(input())):
    num, check = map(int, input().split())
    print('Valid' if bin(num).count('1') % 2 == check else 'Corrupt')