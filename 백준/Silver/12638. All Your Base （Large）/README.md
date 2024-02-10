# [Silver III] All Your Base (Large) - 12638 

[문제 링크](https://www.acmicpc.net/problem/12638) 

### 성능 요약

메모리: 109240 KB, 시간: 116 ms

### 분류

그리디 알고리즘, 수학, 정수론, 문자열

### 제출 일자

2024년 2월 10일 22:47:13

### 문제 설명

<p>In A.D. 2100, aliens came to Earth. They wrote a message in a cryptic language, and next to it they wrote a series of symbols. We've come to the conclusion that the symbols indicate a number: the number of seconds before war begins!</p>

<p>Unfortunately we have no idea what each symbol means. We've decided that each symbol indicates one digit, but we aren't sure what each digit means or what base the aliens are using. For example, if they wrote "ab2ac999", they could have meant "31536000" in base 10 -- exactly one year -- or they could have meant "12314555" in base 6 -- 398951 seconds, or about four and a half days. We are sure of three things: the number is positive; like us, the aliens will never start a number with a zero; and they aren't using unary (base 1).</p>

<p>Your job is to determine the minimum possible number of seconds before war begins.</p>

### 입력 

 <p>The first line of input contains a single integer, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case is a string on a line by itself. The line will contain only characters in the 'a' to 'z' and '0' to '9' ranges (with no spaces and no punctuation), representing the message the aliens left us. The test cases are independent, and can be in different bases with the symbols meaning different things.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100</li>
	<li>The answer will never exceed 10<sup>18</sup></li>
	<li>1 ≤ the length of each line < 61</li>
</ul>

### 출력 

 <p>For each test case, output a line in the following format: </p>

<pre>Case #<strong>X</strong>: <strong>V</strong></pre>

<p>Where <strong>X</strong> is the case number (starting from 1) and <strong>V</strong> is the minimum number of seconds before war begins.</p>

