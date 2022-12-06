for _ in range(int(input())):
    n = int(input())
    print('#' * n)
    if n > 1:
        for _ in range(n-2):
            print('#' + 'J' * (n-2) + '#')
        print('#' * n)
    print('')