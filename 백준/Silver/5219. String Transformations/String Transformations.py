for _ in range(int(input())):
    rules = input().split()
    lhs_list, rhs_list = rules[::2], rules[1::2]
    ans = []
    for word in input().split():
        for lhs, rhs in zip(lhs_list, rhs_list):
            word = word.replace(lhs, rhs, 1)
        ans.append(word)
    print("Transformed strings:", *ans)