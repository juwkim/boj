# [Bronze I] Sums of Sums (Small) - 12048 

[문제 링크](https://www.acmicpc.net/problem/12048) 

### 성능 요약

메모리: 175712 KB, 시간: 400 ms

### 분류

구현(implementation)

### 문제 설명

<p>Alice presented her friend Bob with an array of <strong>N</strong> positive integers, indexed from 1 to <strong>N</strong>. She challenged Bob with many queries of the form "what is the sum of the numbers between these two indexes?" But Bob was able to solve the problem too easily.</p>

<p>Alice took her array and found all <strong>N</strong>*(<strong>N</strong>+1)/2 non-empty subarrays of it. She found the sum of each subarray, and then sorted those values (in nondecreasing order) to create a new array, indexed from 1 to <strong>N</strong>*(<strong>N</strong>+1)/2. For example, for an initial array [2, 3, 2], Alice would generate the subarrays [2], [3], [2], [2, 3], [3, 2], and [2, 3, 2] (note that [2, 2], for example, is <strong>NOT</strong> a subarray). Then she'd take the sums -- 2, 3, 2, 5, 5, 7 -- and sort them to get a new array of [2, 2, 3, 5, 5, 7].</p>

<p>Alice has given the initial array to Bob, along with <strong>Q</strong> queries of the form "what is the sum of the numbers from index <strong>L<sub>i</sub></strong> to <strong>R<sub>i</sub></strong>, inclusive, in the new array?" Now Bob's in trouble! Can you help him out?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case begins with one line with two space-separated integers <strong>N</strong> and <strong>Q</strong>, denoting the number of elements in the initial array and the number of Alice's queries. Then, there is one line with <strong>N</strong> space-separated integers, denoting the elements of Alice's initial array. Finally, there are <strong>Q</strong> more lines with two space-separated integers each: <strong>L<sub>i</sub></strong> and <strong>R<sub>i</sub></strong>, the inclusive index bounds for the i-th query.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 10.</li>
	<li>1 ≤ <strong>Q</strong> ≤ 20.</li>
	<li>1 ≤ each element of the initial array ≤ 100.</li>
	<li>1 ≤ <strong>L<sub>i</sub></strong> ≤ <strong>R<sub>i</sub></strong> ≤ N*(N+1)/2.</li>
	<li>1 ≤ <strong>N</strong> ≤ 10<sup>3</sup>.</li>
</ul>

### 출력 

 <p>For each test case, output one line with <code>Case #x:</code>, where <strong>x</strong> is the test case number (starting from 1). Then output <strong>Q</strong> more lines, each with one integer, representing the answers to the queries (in the order they were asked).</p>

