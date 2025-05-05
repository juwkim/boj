# [Silver I] Wonderful Fours - 7106 

[문제 링크](https://www.acmicpc.net/problem/7106) 

### 성능 요약

메모리: 110736 KB, 시간: 132 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2025년 5월 6일 08:44:13

### 문제 설명

<p>Let us name a set of five decimal digits K5. (Note that numbers may be repeated within this set).</p>

<p>We can say that a natural five-digit number is properly formed from K5 if it is formed by sequentially writing all the digits of K5 in a row in any order (taking each of them exactly once) and this number does not start with zero.</p>

<p>In this way, for example, if K5 contains four digits 1,1,7,0 and 4, then numbers 17140 and 47011 are properly formed from K5, while 17740 is not.</p>

<p>Let us call four natural five-digit numbers s1,s2,s3,s4 a K5 wonderful four, if the following properties are true for them :</p>

<ol>
	<li>s1 is properly formed from K5;</li>
	<li>s2 is properly formed from K5;</li>
	<li>s3 is properly formed from K5;</li>
	<li>s4 is properly formed from K5;</li>
	<li>s1, s2, s3 un s4 are all different numbers;</li>
	<li>s1+ s2 + s3 = s4</li>
</ol>

<p>The task is to compute how many different K5 wonderful fours can be formed from the five digits contained by the set K5 given in the input data. (Change of order of numbers within a wonderful four does not form a new wonderful four).</p>

### 입력 

 Empty

### 출력 

 Empty

