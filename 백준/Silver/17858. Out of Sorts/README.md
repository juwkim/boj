# [Silver IV] Out of Sorts - 17858 

[문제 링크](https://www.acmicpc.net/problem/17858) 

### 성능 요약

메모리: 190576 KB, 시간: 296 ms

### 분류

이분 탐색(binary_search), 구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Ann Logan is fascinated with finite sequences of integers. She is particularly interested in sequences of the form x<sub>1</sub>, x<sub>2</sub>, . . . , x<sub>n</sub> where:</p>

<ul>
	<li>x<sub>i</sub> = (ax<sub>i−1</sub> + c) mod m,</li>
	<li>n, m, a, and c are positive integer constants,</li>
	<li>x<sub>0</sub> is a non-negative integer constant, and</li>
	<li>all n values are unique.</li>
</ul>

<p>For example, if n = 5, m = 8, a = 1, c = 3, and x<sub>0</sub> = 3, the sequence is 6, 1, 4, 7, 2 (x<sub>1</sub> = (1 · 3 + 3) mod 8 = 6, x<sub>2</sub> = (1 · 6 + 3) mod 8 = 1, and so on). Note that she does not consider the initial value x0 to be part of the sequence.</p>

<p>Ann wants to be able to quickly determine, for any integer value, whether or not it appears within a finite sequence of this form. Given values of n, m, a, c, and x<sub>0</sub>, she plans to follow this list of steps:</p>

<ol>
	<li>Generate the sequence x<sub>1</sub>, · · · , x<sub>n</sub> and store it in an array.</li>
	<li>Sort the array.</li>
	<li>Perform a binary search of the array for each integer of interest to her.</li>
</ol>

<p>Ann’s search algorithm, while not the most efficient possible, is pretty straightforward and understandable to anyone familiar with binary search: after calculating the midpoint mid at each step of the calculation (using mid = (low+high)/2), she first checks whether or not the value at location mid is equal to the search value x. If not, she then narrows the search according to whether x is strictly less than or strictly greater than the value at location mid.</p>

<p>Unfortunately, Ann is absent-minded and she lost her list of steps. She managed to remember the first and last step, but . . . she forgot to sort the array before performing her binary search! Needless to say, this means that many values that are in the (unsorted) array will not be found by a binary search, although surprisingly some can. In the example above, both 4 and 7 can be found with Ann’s binary search. How many values can be found for various sequences? Don’t botch it up!</p>

### 입력 

 <p>Input consists of a line containing five integers n, m, a, c, and x<sub>0</sub> (1 ≤ n ≤ 10<sup>6</sup>, 1 ≤ m, a, c ≤ 2<sup>31</sup> − 1, 0 ≤ x<sub>0</sub> ≤ 2<sup>31</sup> − 1), where n is the length of the sequence x<sub>1</sub>, . . . , x<sub>n</sub> to be generated and m, a, c, and x<sub>0</sub> are the constants used for generating the sequence. All values in the generated sequence are guaranteed to be unique.</p>

### 출력 

 <p>Output the number of sequence values that could be found using Ann’s version of binary search, assuming she forgot to sort the sequence.</p>

