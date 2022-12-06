same = {1: "Habb Yakk", 2: "Dobara", 3: "Dousa",
        4: "Dorgy", 5: "Dabash", 6: "Dosh"}
diff = {1: "Yakk", 2: "Doh", 3: "Seh",
        4: "Ghar", 5: "Bang", 6: "Sheesh"}
for i in range(1, 1+int(input())):
    a, b = sorted(map(int, input().split()))
    if a == b:
        state = same[a]
    elif a == 5 and b == 6:
        state = "Sheesh Beesh"
    else:
        state = ' '.join([diff[b], diff[a]])
    print(f'Case {i}: {state}')