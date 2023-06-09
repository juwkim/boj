# [Bronze III] Roll the Dice - 6856 

[문제 링크](https://www.acmicpc.net/problem/6856) 

### 성능 요약

메모리: 113112 KB, 시간: 120 ms

### 분류

브루트포스 알고리즘, 구현

### 문제 설명

<p>Diana is playing a game with two dice. One die has m sides labelled 1, 2, 3, ..., m. The other die has n sides labelled 1, 2, 3, ..., n. Write a program to determine how many ways can she roll the dice to get the sum 10.</p>

<p>For example, when the first die has 6 sides and the second die has 8 sides, there are 5 ways to get the sum 1</p>

<ul>
	<li>2 + 8 = 10</li>
	<li>3 + 7 = 10</li>
	<li>4 + 6 = 10</li>
	<li>5 + 5 = 10</li>
	<li>6 + 4 = 10</li>
</ul>

### 입력 

 <p>The input is given as two integers. First, the user is prompted for and must enter in the number m (1 ≤ m ≤ 1000). Second, the user is prompted for and must enter the number n (1 ≤ n ≤ 1000).</p>

### 출력 

 <p>The program prints out the number of ways 10 may be rolled on these two dice. Note that in the output, the word “way” should be used if there is only one way to achieve the sum of 10; otherwise, the word “ways” should be used in the output. That is, if there is only one way to get the sum 10, the output should</p>

<pre>There is 1 way to get the sum 10.</pre>

