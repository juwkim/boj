# [Silver III] Scales - 22217 

[문제 링크](https://www.acmicpc.net/problem/22217) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

수학, 정수론

### 제출 일자

2024년 6월 21일 03:09:37

### 문제 설명

<p>You are given an equal arm scales, a set of weight pieces and an object. The pieces are of weight 1,3,9,27,81,..., i.e. the weight of each piece is a power of 3, and for each integer k ≥ 0 there is exactly one piece of weight 3<sup>k</sup>. The object’s weight is m, where m is a positive integer. Your task is to put the object on the left scale pan and to put some pieces on one or both scale pans, so that the scales is in balance.</p>

<p>Write a program that:</p>

<ul>
	<li>reads the object’s weight m from the input,</li>
	<li>calculates which pieces should be put on the left and right scalepan,</li>
	<li>writes the results to the output.</li>
</ul>

### 입력 

 <p>The first line contains one integer m, 1 ≤ m ≤ 10<sup>100</sup>.</p>

### 출력 

 <p>The output should consist of two lines.</p>

<p>The first line should contain information about pieces put on the left scale pan. First number must be non-negative integer - number of pieces put on the left scale pan followed by weights of pieces in increasing order. Numbers must be separated by single spaces.</p>

<p>The second line must contain information about pieces put on the right scale pan in the same format as first line.</p>

