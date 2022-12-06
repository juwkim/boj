# [Bronze II] Rectangles - 8295 

[문제 링크](https://www.acmicpc.net/problem/8295) 

### 성능 요약

메모리: 122244 KB, 시간: 112 ms

### 분류

사칙연산(arithmetic), 브루트포스 알고리즘(bruteforcing), 수학(math)

### 문제 설명

<p>How many rectangles can you find in the figure below?</p>

<p style="text-align: center;"><img alt="" src="" style="width: 150px; height: 100px;"></p>

<p>We have found: 6 rectangles 1 × 1, 4 rectangles 2 × 1, 3 rectangles 1 × 2, 2 rectangles 2 × 2, 2 rectangles 3 × 1 and one rectangle 3 × 2, what gives 18 in total. Clearly, we are interested in rectangles with vertices in grid points, i.e., the points located at the intersections of vertical and horizontal line segments, and having vertical or horizontal sides. The above grid has dimensions 3 × 2.</p>

<p>And how many such rectangles of perimeter at least 6 can be found in the figure? You can find the answer in the Example section.</p>

### 입력 

 <p>The first and only line of the standard input contains three integers: <em>n</em>, <em>m</em> and <em>p</em> (1 ≤ <em>n</em>, <em>m</em> ≤ 100, 4 ≤ <em>p</em> ≤ 2(<em>n</em>+<em>m</em>)), representing the dimensions of the grid and the lower bound for the perimeter of the rectangles.</p>

### 출력 

 <p>In the first line of the standard output your program should output one integer: the number of rectangles with vertices in grid points of the grid <em>n</em> × <em>m</em>, having vertical or horizontal sides and which perimeter is at least <em>p</em>.</p>

