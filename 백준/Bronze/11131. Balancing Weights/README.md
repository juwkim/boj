# [Bronze III] Balancing Weights - 11131 

[문제 링크](https://www.acmicpc.net/problem/11131) 

### 성능 요약

메모리: 122244 KB, 시간: 116 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Ever since you started studying, your whole family have been expecting you to know the answers to a whole lot of difficult questions. What is wrong with my computer? What is the name of Prince Harry’s new girlfriend? Have you seen my new pants? Your grandfather has just found a new problem for you, and you are yet again under the pressure of finding the answers to one of life’s most fundamental questions.</p>

<p>You are given a 20 meter long lever balanced exactly on the middle by a massless support. A number of weights are applied to the lever. You need to figure out which side will drop, if any. Being such a brilliant mind, you immediately notice that each of the weights will contribute to the total torque applied on the lever, and that this will determine the answer. The torque from a single weight is determined by</p>

<p>\[\tau  = m \times d\]</p>

<p>where \(\tau\) is the total torque applied, \(m\) is the mass of the weight and \(d\) is its distance from the center. The lever’s angular acceleration can then be found by the equation</p>

<p>\[\alpha = \tau / I\]</p>

<p>where \(\alpha\) is the angular acceleration and \(I\) is the lever’s moment of inertia. The moment of inertia is given by the function</p>

<p>\[I = \int {r^2dm}\]</p>

<p>where \(r\) is the perpendicular distance to the axis of rotation.</p>

### 입력 

 <p>The first line of input contains a single number T, the number of test cases to follow. Each test case starts with a line containing N, the number of weights in the test case. This is followed by a line containing N numbers, W<sub>1</sub> W<sub>2</sub> ... W<sub>N</sub> the locations of the N weights.</p>

<ul>
	<li>0 < T ≤ 100</li>
	<li>0 < N ≤ 100</li>
	<li>−1000 ≤ W<sub>i</sub> ≤ 1000</li>
	<li>A negative Wi means that the weight is located to the left of the center, while a positive one means that it is located to the right.</li>
	<li>The weight of the lever is exactly 2000 grams, uniformly distributed. Each weight weighs 100 grams.</li>
	<li>Weights are modeled as single point masses.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing Left if the weight tips to the left, Right if the weight tips to the right or Equilibrium if the weight does not tip to any of the sides.</p>

