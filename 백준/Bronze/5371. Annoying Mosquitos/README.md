# [Bronze I] Annoying Mosquitos - 5371 

[문제 링크](https://www.acmicpc.net/problem/5371) 

### 성능 요약

메모리: 116468 KB, 시간: 348 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>Lee wants to go to bed but there are mosquitos on the wall in his room. He knows that they will try to bite him as soon as he is about to fall asleep, as they have been doing for the past couple of days. Since he appreciates the value of a good night sleep very much, he decides enough is enough and gets his fly swatter.</p>

<p>Unfortunately for him he was born with the distinct swatting disadvantage of being completely blind. The insects seem to comprehend this and keep really still to avoid triggering his heightened sense of hearing. Lee has no other choice but to hit the wall randomly, but luckily he’s got a pretty large fly swatter: each swat hits all mosquitos in a square area of 101 by 101 units.</p>

### 입력 

 <p>On the first line one positive number: the number of test cases, at most 100. After that per test case:</p>

<ul>
	<li>one line with an integer n (1 ≤ n ≤ 100): the number of mosquitos on the wall.</li>
	<li>n distinct lines with two space-separated integers x<sub>i</sub> and y<sub>i</sub> (−1 000 ≤ x<sub>i</sub>, y<sub>i</sub> ≤ 1 000): the position of the i-th mosquito.</li>
	<li>one line with an integer m (1 ≤ m ≤ 10 000): the number of swats Lee tries.</li>
	<li>m lines with two space-separated integers x<sub>j</sub> and y<sub>j</sub> (−1 000 ≤ x<sub>j</sub> , y<sub>j</sub> ≤ 1 000): the midpoint of the j-th attempt.</li>
</ul>

### 출력 

 <p>Per test case:</p>

<ul>
	<li>one line with the number of mosquitos that get hit.</li>
</ul>

