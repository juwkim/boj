import sys
input = lambda: sys.stdin.readline().rstrip()

l = ["white Barabashka", "blue book", "red chair", "gray mouse", "green bottle"]
for _ in range(5):
    s = input().replace("'", " ").replace(",", " ").replace(".", " ").replace("-", " ").split()
    word = [item for item in l if item in " ".join(s)]
    assert len(word) <= 1
    if len(word) == 1:
        print(word[0])
    else:
        word = [item for item in l if item.split()[0] not in s and item.split()[1] not in s]
        assert len(word) == 1
        print(word[0])