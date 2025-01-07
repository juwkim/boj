# [Gold IV] Jane's Flower Shop (Large) - 14327 

[문제 링크](https://www.acmicpc.net/problem/14327) 

### 성능 요약

메모리: 110736 KB, 시간: 100 ms

### 분류

이분 탐색, 수학, 매개 변수 탐색

### 제출 일자

2025년 1월 7일 22:48:04

### 문제 설명

<p>Jane plans to open a flower shop in the local flower market. The initial cost includes the booth license, furnishings and decorations, a truck to transport flowers from the greenhouse to the shop, and so on. Jane will have to recoup these costs by earning income. She has estimated how much net income she will earn in each of the following Mmonths.</p>

<p>Jane wants to predict how successful her flower shop will be by calculating the IRR (Internal Rate of Return) for the M-month period. Given a series of (time, cash flow) pairs (i, C<sub>i</sub>), the IRR is the compound interest rate that would make total cash exactly 0 at the end of the last month. The higher the IRR is, the more successful the business is. If the IRR is lower than the inflation rate, it would be wise not to start the business in the first place.</p>

<p>For example, suppose the initial cost is <span>$</span>10,000 and the shop runs for 3 months, with net incomes of <span>$</span>3,000, <span>$</span>4,000, and <span>$</span>5,000, respectively. Then the IRR r is given by:</p>

<p><img src="https://onlinejudgeimages.s3.amazonaws.com/problem/14326/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C%20(7).png"></p>

<p>In this case, there is only one rate (~=8.8963%) that satisfies the equation.</p>

<p>Help Jane to calculate the IRR for her business. It is guaranteed that -1 < r < 1, and there is exactly one solution in each test case.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a positive integer M: the number of months that the flower shop will be open. The next line contains M + 1 non-negative integers C<sub>i</sub> (0 ≤ i ≤ M). Note that C<sub>0</sub>represents the initial cost, all the remaining C<sub>i</sub>s are profits, the shop will always either make a positive net profit or zero net profit in each month, and will never have negative profits.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ T ≤ 100.</li>
	<li>C<sub>0</sub> > 0.</li>
	<li>0 ≤ C<sub>i</sub> ≤ 1,000,000,000.</li>
	<li>1 ≤ M ≤ 100.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is a floating-point number: the IRR of Jane's business. <code>y</code>will be considered correct if it is within an absolute  or relative error of 10<sup>-9</sup> of the correct answer.</p>

