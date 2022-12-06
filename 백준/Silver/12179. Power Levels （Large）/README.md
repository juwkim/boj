# [Silver II] Power Levels (Large) - 12179 

[문제 링크](https://www.acmicpc.net/problem/12179) 

### 성능 요약

메모리: 32904 KB, 시간: 152 ms

### 분류

임의 정밀도 / 큰 수 연산(arbitrary_precision), 구현(implementation), 수학(math), 시뮬레이션(simulation)

### 문제 설명

<p>A <em>multifactorial</em> -- that is, a number N followed by some nonzero number E of exclamation points -- is defined as the product of all <strong>positive</strong> numbers (N - K*E) for which K is a nonnegative integer. Normal factorials meet the definition of multifactorials, for example:<br>
<br>
5! = 5 * (5-1) * (5-2) * (5-3) * (5-4) = 120<br>
<br>
Here are the other multifactorials of 5:<br>
<br>
5!! equals 5 * (5-2) * (5-4) = 15<br>
<br>
5!!! equals 5 * (5-3) = 10<br>
<br>
5!!!! equals 5 * (5-4) = 5<br>
<br>
5 followed by five or more !s = 5<br>
<br>
5 with no exclamation points is not considered a multifactorial.<br>
<br>
The villainous Anima and her underling Minera love three things: multifactorials, yelling "IT'S OVER 9000" followed by some number of exclamation points, and going around the universe looking for people to fight.<br>
<br>
When Anima and Minera encounter a potential opponent, Anima asks Minera to use her scanner device to determine the opponent's power level, which is always a positive integer that does not begin with any leading zeroes. Today, the display on Minera's scanner is blurry, and she can only tell Anima the number of digits <strong>D</strong> in the opponent's power level, and not what any of those digits are.<br>
<br>
Anima wants to yell IT'S OVER followed by a multifactorial of 9000 to accurately describe the opponent's power level. She will never yell something that might not be true, and she will never use more exclamation points than she needs to. For example, if <strong>D</strong> = 31682, Anima can't yell IT'S OVER 9000!, because she knows that 9000! also has 31682 digits and the opponent's power level might be a 31682-digit number that is less than or equal to 9000!. However, since 9000!! has fewer than 31682 digits, she can be confident that the opponent's power level is greater than 9000!!, so IT'S OVER 9000!! is guaranteed to be true. Although the opponent's power level is also definitely greater than 9000!!!, 9000!!!!, and so on, she won't use more exclamation points than she needs to. So, in this example, she will yell IT'S OVER 9000!!<br>
<br>
If there is no multifactorial of 9000 that is definitely less than the opponent's power level, Anima will remain dramatically silent. We represent dramatic silence as an ellipsis: <code>...</code><br>
<br>
What should Anima say?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> lines follow. Each contains a positive integer <strong>D</strong>, the number of digits in an opponent's power level.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>D</strong> ≤ 100000.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is either <code>...</code> if Anima must remain silent, or <code>IT'S OVER 9000</code> followed by some positive number of exclamation points. Make sure your output exactly matches these specifications. You may wish to copy our apostrophe character into your code to avoid possible Unicode issues.</p>

