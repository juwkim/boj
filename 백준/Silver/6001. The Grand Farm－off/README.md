# [Silver IV] The Grand Farm-off - 6001 

[문제 링크](https://www.acmicpc.net/problem/6001) 

### 성능 요약

메모리: 190908 KB, 시간: 2836 ms

### 분류

수학(math), 정렬(sorting)

### 문제 설명

<p>Farmer John owns 3*N (1 <= N <= 500,000) cows surprisingly numbered 0..3*N-1, each of which has some associated integer weight W_i (1 <= W_i <= d). He is entering the Grand Farm-off, a farming competition where he shows off his cows to the greater agricultural community.</p>

<p>This competition allows him to enter a group of N cows. He has given each of his cows a utility rating U_i (1 <= U_i <= h), which represents the usefulness he thinks that a particular cow will have in the competition, and he wants his selection of cows to have the maximal sum of utility.</p>

<p>There might be multiple sets of N cows that attain the maximum utility sum. FJ is afraid the competition may impose a total weight limit on the cows in the competition, so a secondary priority is to bring lighter weight competition cows.</p>

<p>Help FJ find a set of N cows with minimum possible total weight among the sets of N cows that maximize the utility, and print the remainder when this total weight is divided by M (10,000,000 <= M <= 1,000,000,000).</p>

<p>Note: to make the input phase faster, FJ has derived polynomials which will generate the weights and utility values for each cow. For each cow 0 <= i < 3*N,</p>

<pre>       W_i = (a*i^5+b*i^2+c) mod d
 and   U_i = (e*i^5+f*i^3+g) mod h</pre>

<p>with reasonable ranges for the coefficients (0 <= a <= 1,000,000,000; 0 <= b <= 1,000,000,000; 0 <= c <= 1,000,000,000; 0 <= e <= 1,000,000,000; 0 <= f <= 1,000,000,000; 0 <= g <= 1,000,000,000; 10,000,000 <= d <= 1,000,000,000; 10,000,000 <= h <= 1,000,000,000).</p>

<p>The formulae do sometimes generate duplicate numbers; your algorithm should handle this properly.</p>

### 입력 

 <ul>
	<li>Line 1: Ten space-separated integers: N, a, b, c, d, e, f, g, h, and M</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single integer representing the lowest sum of the weights of the N cows with the highest net utility.</li>
</ul>

<p> </p>

