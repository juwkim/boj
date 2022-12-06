while (s:=input()) != '-1':
    nums = [*map(int, s.split())][:-1]
    print(sum(2 * i in nums for i in nums))