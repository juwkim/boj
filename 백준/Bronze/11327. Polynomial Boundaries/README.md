# [Bronze I] Polynomial Boundaries - 11327 

[문제 링크](https://www.acmicpc.net/problem/11327) 

### 성능 요약

메모리: 28776 KB, 시간: 76 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>Yraglac's math assignment is boring. Mainly, because it involves calculations, which are -- in his mind -- meant for lesser beings like computers and people who cut the line-up at the cafeteria. So, he decided to write a program to do his assignment for him. Ater all, it's not cheating, right?</p>

<p>Yraglac's assignment is to determine if a point is inside a shape or not. Instead of the shape being defined in terms of straight lines, these shapes instead have sides defined by polynomials. Other than that, point inclusion is defined exactly the same way as for ordinary polygons.</p>

<p>To make the job of the program easier, Yraglac is willing to rotate the shape (and the point) so that only one "side" has to be considered at once, and such that the polynomial is oriented with respect to the x-axis. Then, a point is considered "inside" if its y-coordinate is less than the evaluation of the polynomial at its x-coordinate.</p>

<p>Unfortunately, Yraglac hasn't been attending his computer science classes enough, and so he's a little bit stuck. Can you implement the program for Yraglac?</p>

### 입력 

 <p>The input consists of multiple test cases. Each test case consists of a polynomial description and one point. The test case begins with an integer 0 < <strong>N</strong> < 9 (the degree of the polynomial, minus one), followed by <strong>N</strong> integers, -100 < <strong>a</strong><sub>0</sub>, <strong>a</strong><sub>1</sub>, ..., <strong>a</strong><sub>N-1</sub> < 100, the polynomial coefficients for powers of <strong>x</strong> in the polynomial.</p>

<p>On the next line is a point description, as two integers <strong>x</strong> and <strong>y</strong>, the X and Y coordinates of the point. These are such that -10 < <strong>x</strong> < 10 and |<strong>y</strong>| < 10<sup>9</sup>.</p>

<p>The input ends with a zero.</p>

### 출력 

 <p>Output "Inside" if the point is below the side drawn by the polynomial, "On" if the point is exactly on the polynomial edge, and "Outside" otherwise.</p>

