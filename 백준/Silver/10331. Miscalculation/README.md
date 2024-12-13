# [Silver II] Miscalculation - 10331 

[문제 링크](https://www.acmicpc.net/problem/10331) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

사칙연산, 수학, 파싱, 문자열

### 제출 일자

2024년 12월 14일 06:01:29

### 문제 설명

<p>Bob is an elementary schoolboy, not so good at mathematics. He found Father’s calculator and tried cheating on his homework using it. His homework was calculating given expressions containing multiplications and additions. Multiplications should be done prior to additions, of course, but the calculator evaluates the expression from left to right, neglecting the operator precedence. So his answers may be the result of either of the following two calculation rules.</p>

<ul>
	<li>Doing multiplication before addition</li>
	<li>Doing calculation from left to right neglecting the operator precedence</li>
</ul>

<p>Write a program that tells which of the rules is applied from an expression and his answer.</p>

<p>An expression consists of integers and operators. All the integers have only one digit, from 0 to 9. There are two kinds of operators + and *, which represent addition and multiplication, respectively.</p>

<p>The following is an example expression.</p>

<p style="text-align: center;">1+2*3+4</p>

<p>Calculating this expression with the multiplication-first rule, the answer is 11, as in Sample Input 1. With the left-to-right rule, however, the answer will be 13 as shown in Sample Input 2.</p>

<p>There may be cases in which both rules lead to the same result and you cannot tell which of the rules is applied. Moreover, Bob sometimes commits miscalculations. When neither rules would result in Bob’s answer, it is clear that he actually did.</p>

### 입력 

 <p>The input consists of a single test case specified with two lines. The first line contains the expression to be calculated. The number of characters of the expression is always odd and less than or equal to 17. Each of the odd-numbered characters in the expression is a digit from ‘0’ to ‘9’. Each of the even-numbered characters is an operator ‘+’ or ‘*’. The second line contains an integer which ranges from 0 to 999999999, inclusive. This integer represents Bob’s answer for the expression given in the first line.</p>

### 출력 

 <p>Output one of the following four characters:</p>

<ul>
	<li><code>M</code> When only the multiplication-first rule results Bob’s answer.</li>
	<li><code>L</code> When only the left-to-right rule results Bob’s answer.</li>
	<li><code>U</code> When both of the rules result Bob’s answer.</li>
	<li><code>I</code> When neither of the rules results Bob’s answer.</li>
</ul>

