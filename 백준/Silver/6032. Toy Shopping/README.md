# [Silver V] Toy Shopping - 6032 

[문제 링크](https://www.acmicpc.net/problem/6032) 

### 성능 요약

메모리: 119248 KB, 시간: 208 ms

### 분류

그리디 알고리즘(greedy), 구현(implementation), 정렬(sorting)

### 문제 설명

<p>Bessie wants some toys. She's been saving her allowance for years, and has an incredibly huge stash. However, she is quite frugal and wants to get the best value for her cash. In fact, she has decided only to buy exactly three different toys of the N (3 <= N <= 25,000) offered at the Bovine Plaything Palace.</p>

<p>Toy i brings Bessie J_i (0 <= J_i <= 1,000,000) microbundles of joy and has price P_i (0 < P_i <= 100,000,000). Bessie has enough money to buy any three toys that she chooses.</p>

<p>Bessie wants to maximize the sum of her happy-frugal metric (which is calculated as J_i/P_i -- joy divided by price) for the three toys she chooses. Help Bessie decide which toys she should buy. The answer is guaranteed to be unique.</p>

<p>Assume that the Bovine Plaything Palace offers 6 different toys for Bessie:</p>

<pre>        i    Joy       Price       Happy-Frugal Metric
        -    ---       -----       -------------------
        1      0        521               0.00000
        2    442        210               2.10476...
        3    119        100               1.19000
        4    120        108               1.11111...
        5    619        744               0.83198...
        6     48         10               4.80000</pre>

<p>Bessie would choose toy 6 (HFM = 4.80), toy 2 (HFM = 2.10), and toy 3 (HFM = 1.19).</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
	<li>Lines 2..N+1: Line i+1 contains two space-separated integers: J_i and P_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: The total price that Bessie will have to pay</li>
	<li>Lines 2..4: In descending order sorted by the happy-frugal metric, the 1-based index of the toys that Bessie should buy, one per line</li>
</ul>

<p> </p>

