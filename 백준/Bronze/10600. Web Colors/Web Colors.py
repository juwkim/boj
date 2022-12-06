colors = {(255, 255, 255): 'White', (192, 192, 192): 'Silver', (128, 128, 128): 'Gray', (0, 0, 0): 'Black', (255, 0, 0): 'Red', (128, 0, 0): 'Maroon', (255, 255, 0): 'Yellow', (128, 128, 0): 'Olive', (0, 255, 0): 'Lime', (0, 128, 0): 'Green', (0, 255, 255): 'Aqua', (0, 128, 128): 'Teal', (0, 0, 255): 'Blue', (0, 0, 128): 'Navy', (255, 0, 255): 'Fuchsia', (128, 0, 128): 'Purple'}

while (s:= input()) != '-1 -1 -1':
    r, g, b = map(int, s.split())
    print(colors[min(colors, key=lambda x: (x[0] - r)**2 + (x[1] - g)**2 + (x[2] - b)**2)])