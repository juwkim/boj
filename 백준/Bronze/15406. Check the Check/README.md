# [Bronze II] Check the Check - 15406 

[문제 링크](https://www.acmicpc.net/problem/15406) 

### 성능 요약

메모리: 28776 KB, 시간: 5844 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p style="text-align:center"><img alt="" src="" style="height:222px; width:166px"></p>

<p>As a tourist in Paris, you were told you should always carefully check the itemized bill (also called check) that is presented to you at the end of a meal with the list of what you ordered and the total price. Indeed, it is not uncommon for these bills to be handwritten, and for the total to be computed by hand by the waiter. You definitely do not want to overpay for your meal, and will protest if there is a mistake in the restaurant’s favor. However, if the restaurant gives you a discount, you will not complain about it.</p>

<p>Write a program that decides whether you should pay the total amount presented on the check, or protest about the check.</p>

### 입력 

 <p>The input is formed of 2n + 2 lines:</p>

<ul>
	<li>lines 2k + 1 for 0 ≤ k ≤ n − 1 consist of the name of the ordered dish d<sub>k</sub>;</li>
	<li>lines 2k + 2 for 0 ≤ k ≤ n − 1 consist of the integer price p<sub>k</sub> of d<sub>k</sub> in euros, and the number c<sub>k</sub> of orders for d<sub>k</sub>, separated by a space;</li>
	<li>line 2n + 1 consists of the word “TOTAL”;</li>
	<li>line 2n + 2 consists of the integer total T in euros computed by the waiter.</li>
</ul>

<p>Limits</p>

<ul>
	<li>For every 0 ≤ k ≤ n − 1:
	<ul>
		<li>d<sub>k</sub> has at most 1 000 characters, and is never equal to “TOTAL”;</li>
		<li>0 ≤ p<sub>k</sub> ≤ 1 000;</li>
		<li>0 ≤ c<sub>k</sub> ≤ 10;</li>
	</ul>
	</li>
	<li>0 ≤ n ≤ 100 000;</li>
	<li>T ≤ 2 000 000 000.</li>
</ul>

### 출력 

 <p>The output should consist of a single line, whose content is either “PAY” (if the displayed total is less than or equal to the actual total) or “PROTEST” (otherwise).</p>

