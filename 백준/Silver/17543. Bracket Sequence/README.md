# [Silver II] Bracket Sequence - 17543 

[문제 링크](https://www.acmicpc.net/problem/17543) 

### 성능 요약

메모리: 151080 KB, 시간: 168 ms

### 분류

자료 구조, 구현, 스택

### 제출 일자

2024년 12월 16일 05:35:12

### 문제 설명

<p><img alt="" src="https://upload.acmicpc.net/1512ee25-a2eb-4fbe-b914-965e1b2536e8/-/preview/" style="width: 171px; height: 209px; float: right;">Two great friends, Eddie John and Kris Cross, are attending the Brackets Are Perfection Conference. They wholeheartedly agree with the main message of the conference and they are delighted with all the new things they learn about brackets.</p>

<p>One of these things is a bracket sequence. If you want to do a computation with + and ×, you usually write it like so:</p>

<p style="text-align: center;">(2 × (2 + 1 + 0 + 1) × 1) + 3 + 2.</p>

<p>The brackets are only used to group multiplications and additions together. This means that you can remove all the operators, as long as you remember that addition is used for numbers outside any parentheses! A bracket sequence can then be shortened to</p>

<p style="text-align: center;">( 2 ( 2 1 0 1 ) 1 ) 3 2.</p>

<p>That is much better, because it saves on writing all those operators. Reading bracket sequences is easy, too. Suppose you have the following bracket sequence</p>

<p style="text-align: center;">5 2 ( 3 1 ( 2 2 ) ( 3 3 ) 1 ).</p>

<p>You start with addition, so this is the same as the following:</p>

<p style="text-align: center;">5 + 2 + ( 3 1 ( 2 2 ) ( 3 3 ) 1 ).</p>

<p>You know the parentheses group a multiplication, so this is equal to</p>

<p style="text-align: center;">5 + 2 + (3 × 1 × ( 2 2 ) × ( 3 3 ) × 1).</p>

<p>Then there is another level of parentheses: that groups an operation within a multiplication, so the operation must be addition.</p>

<p style="text-align: center;">5 + 2 + (3 × 1 × (2 + 2) × (3 + 3) × 1) = 5 + 2 + (3 × 1 × 4 × 6 × 1) = 5 + 2 + 72 = 79.</p>

<p>Since bracket sequences are so much easier than normal expressions with operators, it should be easy to evaluate some big ones. We will even allow you to write a program to do it for you.</p>

<p>Note that ( ) is not a valid bracket sequence, nor a subsequence of any valid bracket sequence.</p>

### 입력 

 <ul>
	<li>One line containing a single integer 1 ≤ n ≤ 3 · 10<sup>5</sup>.</li>
	<li>One line consisting of n tokens, each being either (, ), or an integer 0 ≤ x < 10<sup>9</sup> + 7. It is guaranteed that the tokens form a bracket sequence.</li>
</ul>

### 출력 

 <p>Output the value of the given bracket sequence. Since this may be very large, you should print it modulo 10<sup>9</sup> + 7.</p>

