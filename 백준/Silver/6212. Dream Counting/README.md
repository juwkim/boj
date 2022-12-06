# [Silver V] Dream Counting - 6212 

[문제 링크](https://www.acmicpc.net/problem/6212) 

### 성능 요약

메모리: 116740 KB, 시간: 688 ms

### 분류

브루트포스 알고리즘(bruteforcing), 수학(math)

### 문제 설명

<p>Bessie was daydreaming one day as she drifted between wakefulness and that delicious drowsiness that we all feel when we are tired. For a moment, she counted sheep as couldn't quite sleep. Bessie's mind is razor sharp and visualizes the numbers as she counts. She started noticing the digits and wondered: how many instances of each digit appear in a counting sequence?</p>

<p>Write a program to answer this question. Given two integers M and N (1 <= M <= N <= 2,000,000,000 and N-M <= 500,000), how many of occurrences of each digit appear?</p>

<p>Consider the sequence 129..137: 129, 130, 131, 132, 133, 134, 135, 136, 137. Count the digits to find:</p>

<pre>   1x0      1x5
  10x1      1x6
   2x2      1x7
   9x3      0x8
   1x4      1x9</pre>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: M and N</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: Ten space-separated integers that are the counts of the number of each digit (0..9) that appears while counting through the sequence.</li>
</ul>

