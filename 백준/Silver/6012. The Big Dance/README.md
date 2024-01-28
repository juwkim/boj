# [Silver III] The Big Dance - 6012 

[문제 링크](https://www.acmicpc.net/problem/6012) 

### 성능 요약

메모리: 109240 KB, 시간: 112 ms

### 분류

재귀

### 제출 일자

2024년 1월 28일 09:37:45

### 문제 설명

<p>Bessie and the herd, N (1 <= N <= 2,200) conveniently numbered 1..N cows in all, have gone to a dance where plenty of bulls are available as dancing partners. This dance is known as the "odd cow out" dance because of the way cows are chosen to dance with bulls.</p>

<p>The cows are lined up in numerical order and the 'middle' point is chosen. It either divides the line of cows exactly in half or it is chosen so that the first set of cows has just one more cow in it than the second set. If exactly two cows are in the set, they are chosen to dance with bulls.  If one cow is in the set, she is sent home with a consolation prize of a beautiful rose.</p>

<p>If the set has more than two cows in it, the process is repeated perhaps again and again until sets with just one or two cows emerge.</p>

<p>The two cow ID numbers are multiplied together and added to a global sum.</p>

<p>Given the number of cows at the dance, compute the global sum after all the eligible cows are chosen.</p>

<p>Consider a dance with 11 cows numbered 1..11. Here is the sequence of dividing them:</p>

<pre>1     2     3     4     5     6  |  7     8     9     10     11

    1     2     3  |  4     5     6

        1     2  |  3
                1  2        => 1*2=2 added to sum -> sum=2
                3           => sent home with rose

        4     5  |  6
                4  5        => 4*5=20 added to sum -> sum=22
                6           => sent home with rose

    7     8     9  | 10    11

        7     8  |  9
                7  8        => 7*8=56 added to sum -> sum=78
                9           => sent home with rose
        10    11            => 10*11=110 added to sum -> sum=188</pre>

<p>So the sum for this dance would be 188.</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the sum computed as prescribed.</li>
</ul>

<p> </p>

