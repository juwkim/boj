# [Silver IV] Skewed Sorting - 5985 

[문제 링크](https://www.acmicpc.net/problem/5985) 

### 성능 요약

메모리: 114328 KB, 시간: 120 ms

### 분류

분할 정복(divide_and_conquer), 구현(implementation), 재귀(recursion)

### 문제 설명

<p>Farmer John has 2^N (1 <= N <= 10) cows, each conveniently labeled with paint on her flank with a number in the range 1..2^N. They are standing in a line in some random order. The first cow in line is cow_1; the second cow in line is cow_2; and so on (1 <= cow_i <= 2^N). Of course, cow_1 is unlikely to carry the painted label 1.</p>

<p>He performs the following algorithm to put them in order.</p>

<ol>
	<li>If there is more than one cow, then partition the cows into two equal-sized sub-groups. Sort the first sub-group using this algorithm and then sort the second sub-group, also using this algorithm.</li>
	<li>Consider the current set of cows to be sorted as an equal-length pair of (potentially huge) base 2^N numbers. If the second number is smaller than the first one, then swap all the elements of the second one with those elements of the first one.</li>
</ol>

<p>The cows would like to know how much distance they cover while moving around during this 'sorting' procedure.</p>

<ul>
	<li>Given the initial configuration of the cows, process the list according to the algorithm above and then print out:</li>
	<li>the sum of the total distances traveled by all cows and</li>
	<li>the final configuration of the cows after this 'sorting' procedure.</li>
</ul>

<p>By way of example, consider this line of 2^3=8 cows:</p>

<pre>        8 5 2 3 4 7 1 6</pre>

<p>First, Farmer John will sort each half of the line separately:</p>

<pre>        8 5 2 3 | 4 7 1 6</pre>

<p>Since each half still has more than one cow, Farmer John will sort those halves separately; starting with the 'first' half:</p>

<pre>        8 5 | 2 3</pre>

<p>Partitioning again, FJ makes</p>

<pre>        8 | 5      and        2 | 3</pre>

<p>each of which can be sorted by second rule, ultimately yielding:</p>

<pre>        5 | 8      and        2 | 3 (<--unchanged)</pre>

<p>The distance traveled by each cow during the first subgroup's sort is 1, so total_distance_moved becomes 2. The second half is already sorted, so the total_distance_moved stays at 2. The new configuration of this sub-group is:</p>

<pre>        5 8 | 2 3</pre>

<p>For step 2 of the algorithm on the subgroup above, we compare the two sides lexicographically (5 8 vs. 2 3). Since the 2 comes before 5, we swap the two elements of the first half with the corresponding elements of the second half, yielding:</p>

<pre>        2 3 5 8</pre>

<p>Each of the four cows moved two spaces in this swap, contributing a total of 8 moves, so total_distance_moved becomes 10.</p>

<p>Consider the other half of the cows; we divide the list of four into two sub-groups:</p>

<pre>        4 7 | 1 6</pre>

<p>Each pair (4, 7) and (1, 6) is already sorted.</p>

<p>Comparing (4 7) to (1 6), since 1 comes before 4, we must swap the two sub-groups:</p>

<pre>        1 6 4 7</pre>

<p>which contributes a total of 8 more moves, bringing total_distanced_move to 18.</p>

<p>After the operations above, the list looks like this (and it's time for step 2 to be performed on the two groups of 4):</p>

<pre>        2 3 5 8 | 1 6 4 7</pre>

<p>Since 1 comes before 2, we must swap the halves, this yielding this configuration:</p>

<pre>        1 6 4 7 2 3 5 8</pre>

<p>Since each of 8 cows moved four units, this contributes a total of 32 more moves, making total_distance_moved become 50</p>

<p>Therefore, the answer is 50 and 1 6 4 7 2 3 5 8.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
	<li>Lines 2..2^N + 1: Line i+1 contains a single integer: cow_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: One integer, the total distance traveled by all the cows</li>
	<li>Lines 2..2^N + 1: Line i+1 will contain one integer: the ith cow in the final configuration</li>
</ul>

<p> </p>

