from collections import Counter
for tc in range(1, 1 + int(input())):
    vote = Counter({"cinema": 0, "cocktail bar": 0, "disco": 0})
    names = set(input().split())
    for name in names:
        match name:
            case "Anne":
                vote["cinema"] += 1
            case "Bob":
                if "Karin" in names and "Dave" not in names and "Edward" not in names and "Anne" in names:
                    vote["disco"] += 1
                elif "Karin" not in names and ("Dave" in names or "Edward" in names or "Anne" not in names):
                    vote["cocktail bar"] += 1
            case "Karin":
                if "Charly" in names:
                    vote["disco"] += 1
                elif "Anne" in names:
                    vote["cinema"] += 1
                else:
                    vote["cocktail bar"] += 1
            case "Dave":
                pass
            case "Charly":
                if "Anne" in names:
                    vote["cinema"] += 1
            case "Edward":
                if "Anne" in names and "Charly" not in names:
                    vote["cocktail bar"] += 1
                else:
                    vote["cinema"] += 1
            case "Frank":
                if "Bob" not in names and "Anne" not in names:
                    vote["cinema"] += 1
                elif "Anne" in names:
                    vote["disco"] += 1
    print(f"Scenario #{tc}:")
    a, b = vote.most_common(2)
    if a[1] == b[1]:
        print("stay at the Hacienda")
    else:
        print(a[0])
    print()