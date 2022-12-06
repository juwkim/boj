# [Bronze II] Loop of Chocolate - 24957 

[문제 링크](https://www.acmicpc.net/problem/24957) 

### 성능 요약

메모리: 113248 KB, 시간: 112 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>Let’s make sweets of a fancy shape that is a loop of chocolate.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 149px; height: 110px;"></p>

<p style="text-align: center;">Figure A.1. A loop of chocolate formed by a union of six spheres</p>

<p>The shape of a loop is formed by a union of a number of spheres of the same size, where every sphere intersects with exactly two others.</p>

<table class="table table-bordered td-center">
	<tbody>
		<tr>
			<td style="width: 50%;"><img alt="" src="" style="width: 149px; height: 110px;"></td>
			<td style="width: 50%;"><img alt="" src="" style="width: 148px; height: 110px;"></td>
		</tr>
		<tr>
			<td style="width: 50%;">(a) Union of four spheres</td>
			<td style="width: 50%;">(b) Four intersections of the four spheres in (a)</td>
		</tr>
		<tr>
			<td colspan="2">Figure A.2. A loop of chocolate formed by a union of four spheres</td>
		</tr>
	</tbody>
</table>

<p>Your job is to write a program that, for given the size and the positions of spheres, computes the total volume of the union of the spheres, i.e., the amount of chocolate required for filling the loop formed by the union.</p>

<p><strong>[Hints]</strong> Two spheres of the same radius $r$ intersect each other when the distance between their centers, $d$, is less than $2r$. The volume of the intersection is known to be $$\frac{2}{3}\pi (r - d/2)^2(2r+d/2)\text{.}$$</p>

<p>The volume of the sphere of radius $r$ is $4\pi r^3/3$.</p>

### 입력 

 <p>The input consists of a single test case of the following format.</p>

<p>$\begin{align*}&n \, r \\ & x_1 \, y_1 \, z_1 \\ & \vdots \\ & x_n \, y_n \, z_n \end{align*}$</p>

<p>$n$ and $r$ are integers. $n$ is the number of spheres ($4 ≤ n ≤ 100$). All the spheres has the same radius $r$ ($2 ≤ r ≤ 100$). $(x_k, y_k, z_k)$ indicates the coordinates of the center of the $k$-th sphere ($k = 1, \dots , n$). All of $x_k$, $y_k$, and $z_k$ are integers between $-100$ and $100$, inclusive.</p>

<p>The $k$-th and the $k + 1$-th spheres intersect each other for $1 ≤ k < n$. The $1$-th and the $n$-th spheres also intersect. No other pairs of spheres intersect.</p>

### 출력 

 <p>Output in a line the volume of the union of the spheres. Relative error of the output should be within $10^{-7}$.</p>

