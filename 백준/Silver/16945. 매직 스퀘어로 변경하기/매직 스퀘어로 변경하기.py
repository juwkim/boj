magics = (
    (4, 9, 2, 3, 5, 7, 8, 1, 6),
    (2, 9, 4, 7, 5, 3, 6, 1, 8),
    (8, 3, 4, 1, 5, 9, 6, 7, 2),
    (4, 3, 8, 9, 5, 1, 2, 7, 6),
    (6, 1, 8, 7, 5, 3, 2, 9, 4),
    (8, 1, 6, 3, 5, 7, 4, 9, 2),
    (2, 7, 6, 9, 5, 1, 4, 3, 8),
    (6, 7, 2, 1, 5, 9, 8, 3, 4)
)
A = [*map(int, open(0).read().split())]
print(min(sum(abs(a - b) for a, b in zip(A, magic)) for magic in magics))