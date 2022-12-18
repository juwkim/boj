for _ in range(int(input())):
 l = [input() for _ in range(3)]
 print(["No", "Yes"][all(l[i] not in (l[(i + 1) % 3][:len(l[i])], l[(i + 2) % 3][:len(l[i])], l[(i + 1) % 3][-len(l[i]):], l[(i + 2) % 3][-len(l[i]):]) for i in range(3))])