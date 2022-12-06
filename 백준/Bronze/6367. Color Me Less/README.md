# [Bronze I] Color Me Less - 6367 

[문제 링크](https://www.acmicpc.net/problem/6367) 

### 성능 요약

메모리: 28776 KB, 시간: 72 ms

### 분류

사칙연산(arithmetic), 브루트포스 알고리즘(bruteforcing), 구현(implementation), 수학(math)

### 문제 설명

<p>A color reduction is a mapping from a set of discrete colors to a smaller one. The solution to this problem requires that you perform just such a mapping in a standard twenty-four bit RGB color space. The input consists of a target set of sixteen RGB color values, and a collection of arbitrary RGB colors to be mapped to their closest color in the target set. For our purposes, an RGB color is defined as an ordered triple (R,G,B) where each value of the triple is an integer from 0 to 255. The distance between two colors is defined as the Euclidean distance between two three-dimensional points. That is, given two colors (R<sub>1</sub>,G<sub>1</sub>,B<sub>1</sub>) and (R<sub>2</sub>,G<sub>2</sub>,B<sub>2</sub>), their distance D is given by the equation</p>

<p>\[D = \sqrt { (R_2-R_1)^2 + (G_2-G_1)^2 + (B_2-B_1)^2 } \]</p>

### 입력 

 <p>The input is a list of RGB colors, one color per line, specified as three integers from 0 to 255 delimited by a single space. The first sixteen colors form the target set of colors to which the remaining colors will be mapped. The input is terminated by a line containing three -1 values.</p>

### 출력 

 <p>For each color to be mapped, output the color and its nearest color from the target set.</p>

