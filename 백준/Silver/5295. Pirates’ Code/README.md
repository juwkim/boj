# [Silver II] Pirates’ Code - 5295 

[문제 링크](https://www.acmicpc.net/problem/5295) 

### 성능 요약

메모리: 110708 KB, 시간: 112 ms

### 분류

브루트포스 알고리즘, 정렬

### 제출 일자

2025년 2월 22일 21:11:47

### 문제 설명

<p>Davy Jones has captured another ship and is smiling contently under the sun. Today is a good day for him. He will get more souls to serve on his crew. The day, however, looks so nice, the sun shining brightly above all and the ocean spilled calmly around, that he decides to be merciful and give some chance to the wretched seamen of the captured ship. He decides to play the following game.</p>

<p>He will line a group of captives in front of him, and then write a number of his choice on each man’s forehead. After that, he wants to check if the set of numbers is 3-free. What does it mean for a set to be 3-free? It means that there are no 3 numbers in the set that form an increasing arithmetic progression (weird games have damned Jones, aye), i.e., a sequence of numbers such that the difference of any two successive members of the sequence is a positive constant, such as {123}, {468}, or {-2, 1, 4}. If the the set of numbers on men’s foreheads is 3-free, the group is free, too (what an irony). However, if not, those who have the numbers of the lexicographically first triple that proves (i.e. is a witness) that the set is not 3-free will serve on Jones’ crew for an eternity.</p>

<p>And you ... You will be Jones’ assistant in this game. Checking each group whether it is 3-free or not. And you’d better check right or you will end up on Jones’ crew as well.</p>

<p>A triple (a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>) is an increasing arithmetic progression if a<sub>2</sub> − a<sub>1</sub> = a<sub>3</sub> − a<sub>2</sub>, and a<sub>2</sub> − a<sub>1</sub> > 0. A triple (a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>) is lexicographically smaller than (b<sub>1</sub>, b<sub>2</sub>, b<sub>3</sub>) if</p>

<ul>
	<li>a<sub>1</sub> < b<sub>1</sub>, or</li>
	<li>a<sub>1</sub> = b<sub>1</sub> and a<sub>2</sub> < b<sub>2</sub>, or</li>
	<li>a<sub>1</sub> = b<sub>1</sub>, a<sub>2</sub> = b<sub>2</sub> and a<sub>3</sub> < b<sub>3</sub>.</li>
</ul>

<p>Note that you will be looking at triples (a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>) of increasing order, i.e. a<sub>1</sub> ≤ a<sub>2</sub> ≤ a<sub>3</sub>. The numbers on men’s foreheads need not be in increasing order though.</p>

### 입력 

 <p>Input consists of a single line with the numbers written on the captured men’s foreheads. The first number of the line denotes how many men are there in the group and should not be included in the sequence.</p>

### 출력 

 <p>Output should consist of a single line. If the sequence of numbers in the input is 3-free, output “Sequence is 3-free.” If the sequence is not 3-free, output “Sequence is not 3-free. Witness: w<sub>1</sub>, w<sub>2</sub>, w<sub>3</sub>.” (note the intervals after the first dot and the colon), where w<sub>1</sub>, w<sub>2</sub>, w<sub>3</sub> is the lexicographically first witness that the sequence is not 3-free.</p>

