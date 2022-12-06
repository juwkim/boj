# [Bronze I] Claustrophobic Cows - 6003 

[문제 링크](https://www.acmicpc.net/problem/6003) 

### 성능 요약

메모리: 115192 KB, 시간: 216 ms

### 분류

브루트포스 알고리즘(bruteforcing), 기하학(geometry), 피타고라스 정리(pythagoras)

### 문제 설명

<p>Farmer John has acquired a set of N (2 <= N <= 2,000) touchy cows who are conveniently numbered 1..N. They really hate being too close to other cows. A lot.</p>

<p>FJ has recorded the integer X_i,Y_i coordinates of every cow i (1 <= X_i <= 100,000; 1 <= Y_i <= 100,000).</p>

<p>Among all those cows, exactly two of them are closest together. FJ would like to spread them out a bit. Determine which two are closest together and print their cow id numbers (i) in numerical order.</p>

<p>By way of example, consider this field of cows (presented on a typewriter grid that has slightly different proportions than you might expect):</p>

<pre>                    10 | . . . . . . . 3 . . . . .
                     9 | . 1 . . 2 . . . . . . . .
                     8 | . . . . . . . . . . . . .
                     7 | . . . . . . . . . . 4 . .
                     6 | . . . . . . 9 . . . . . .
                     5 | . 8 . . . . . . . . . . .
                     4 | . . . . . 7 . . . . . . .
                     3 | . . . . . . . . . 5 . . .
                     2 | . . . . . . . . . . . . .
                     1 | . . . . 6 . . . . . . . .
                     0 ---------------------------
                                           1 1 1 1
                       0 1 2 3 4 5 6 7 8 9 0 1 2 3</pre>

<p>Quick visual inspection shows that cows 7 and 9 are closest together (the distance separating them is sqrt(1*1+2*2) = sqrt(5), so the output would be '7 9' on a single line (without quotes, of course).</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
	<li>Lines 2..N+1: Line i contains the coordinates of cow i expressed as two space-separated integers: X_i and Y_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: The two numerical IDs of the closest pair of cows (sorted)</li>
</ul>

<p> </p>

