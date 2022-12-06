# [Bronze II] Comfy Deviations - 21301 

[문제 링크](https://www.acmicpc.net/problem/21301) 

### 성능 요약

메모리: 46236 KB, 시간: 152 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>According to Wikipedia, standard deviation is a number used to tell how measurements for a group are spread out from the average (mean or expected value). A low standard deviation means that most of the numbers are close to the average, while a high standard deviation means that the numbers are more spread out. For this problem, you will read in 10 temperature values and use the standard deviation to determine if values are close to the mean temperature. The formula for calculating the standard deviation is:</p>

<p>$$s_t = \sqrt{\frac{\sum_{i=1}^{n}{(t_i-\overline{t})^2}}{n-1}}$$</p>

<ul>
	<li>$s_t$ = Standard deviation of temperature values</li>
	<li>$n$ = The number of data points (10 in this case)</li>
	<li>$t_i$ = Each of the input temperature values</li>
	<li>$\overline{t}$ = The average (mean) of all 10 input values.</li>
</ul>

### 입력 

 <p>Input consists of a single line containing 10 space separated floating point values representing the temperature values to check.</p>

<p>Each temperature value, $t_1 \dots t_{10}$ will be in the range ($68 \le t \le 80$)</p>

### 출력 

 <p>The output consists of a single line that has the string <code>COMFY</code> if the standard deviation of the input values is ≤ 1.0 or <code>NOT COMFY</code> if the standard deviation of the input values is > 1.0.</p>

