# [Silver V] Flat Earth - 19250 

[문제 링크](https://www.acmicpc.net/problem/19250) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

기하학(geometry), 3차원 기하학(geometry_3d), 수학(math)

### 문제 설명

<p>The education system has let you down once again -- your proposal to include the Flat Earth model into the high school program has been rejected for the sixth time in a row. The corrupt Round-Earth scientists refuse to listen to your arguments, and ignore the piles of data that support your claims. It is time to settle this conflict once and for all. You have traveled all around the globe, and met with top Flat Earth scientists. Together, you devised a brilliant plan.</p>

<p>For the sake of contradiction, suppose that Earth is a sphere in the three-dimensional space. Then, assuming the sky is an infinite plane in the space, such an Earth would clearly cast a shadow on it! This shadow would be an orthogonal projection of Earth onto the sky. Since in reality there is no visible shadow on the sky, we reach a contradiction.</p>

<p>All that is left is to perform the calculations. Given the center and radius of Earth, as well as the equation of the sky-plane in the form $ax + by + cz + d = 0$, determine the area of an orthogonal projection of Earth onto the sky. Note that in some of your experiments Earth may intersect the sky -- you wouldn't like to introduce too many unnecessary assumptions, would you?</p>

### 입력 

 <p>The first line of input contains the number of test cases $z$ ($1 \leq z \leq 10$). The descriptions of the test cases follow.</p>

<p>Every test case is described with a line containing eight integers $x$, $y$, $z$, $r$, $a$, $b$, $c$, $d$. They denote the coordinates of Earth's center, it's radius, and the sky's equation, respectively. All numbers are between $1$ and $1000$ inclusive.</p>

### 출력 

 <p>For each test case output one number: the area of the projection. Your answer will be considered correct if the absolute or relative error does not exceed $10^{-6}$.</p>

