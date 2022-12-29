# [Silver IV] Unloaded Die - 15120 

[문제 링크](https://www.acmicpc.net/problem/15120) 

### 성능 요약

메모리: 113112 KB, 시간: 104 ms

### 분류

그리디 알고리즘(greedy), 수학(math), 확률론(probability)

### 문제 설명

<p>Consider a six-sided die, with sides labeled 1 through 6. We say the die is fair if each of its sides is equally likely to be face up after a roll. We say the die is loaded if it isn’t fair. For example, if the side marked 6 is twice as likely to come up as than any other side, we are dealing with a loaded die.</p>

<p>For any die, define the expected result of rolling the die to be equal to the average of the values of the sides, weighted by the probability of those sides coming up. For example, all six sides of a fair die are equally likely to come up, and thus the expected result of rolling it is (1 + 2 + 3 + 4 + 5 + 6)/6 = 3.5.</p>

<p>You are given a loaded die, and you would like to unload it to make it more closely resemble a fair die. To do so, you can erase the number on one of the sides, and replace it with a new number which does not need to be an integer or even positive. You want to do so in such a way that</p>

<ul>
	<li>The expected result of rolling the die is 3.5, just like a fair die.</li>
	<li>The difference between the old label and the new label on the side you change is as small as possible.</li>
</ul>

### 입력 

 <p>The input consists of a single line containing six space-separated nonnegative real numbers v<sub>1</sub> . . . v<sub>6</sub>, where v<sub>i</sub> represents the probability that side i (currently labeled by the number i) is rolled.</p>

<p>It is guaranteed that the given numbers will sum to 1.</p>

### 출력 

 <p>Print, on a single line, the absolute value of the difference between the new label and old label, rounded and displayed to exactly three decimal places.</p>

