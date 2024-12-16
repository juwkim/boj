# [Silver II] Ample Syrup (Small) - 14809 

[문제 링크](https://www.acmicpc.net/problem/14809) 

### 성능 요약

메모리: 109544 KB, 시간: 92 ms

### 분류

브루트포스 알고리즘, 기하학

### 제출 일자

2024년 12월 17일 08:20:21

### 문제 설명

<p>The kitchen at the Infinite House of Pancakes has just received an order for a stack of <strong>K</strong>pancakes! The chef currently has <strong>N</strong> pancakes available, where <strong>N</strong> ≥ <strong>K</strong>. Each pancake is a cylinder, and different pancakes may have different radii and heights.</p>

<p>As the sous-chef, you must choose <strong>K</strong> out of the <strong>N</strong> available pancakes, discard the others, and arrange those <strong>K</strong> pancakes in a stack on a plate as follows. First, take the pancake that has the largest radius, and lay it on the plate on one of its circular faces. (If multiple pancakes have the same radius, you can use any of them.) Then, take the remaining pancake with the next largest radius and lay it on top of that pancake, and so on, until all <strong>K</strong> pancakes are in the stack and the centers of the circular faces are aligned in a line perpendicular to the plate, as illustrated by this example:</p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14809/1.png" style="height:136px; width:320px"></p>

<p>You know that there is only one thing your diners love as much as they love pancakes: syrup! It is best to maximize the total amount of exposed pancake surface area in the stack, since more exposed pancake surface area means more places to pour on delicious syrup. Any part of a pancake that is not touching part of another pancake or the plate is considered to be exposed.</p>

<p>If you choose the <strong>K</strong> pancakes optimally, what is the largest total exposed pancake surface area you can achieve?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each begins with one line with two integers <strong>N</strong> and <strong>K</strong>: the total number of available pancakes, and the size of the stack that the diner has ordered. Then, <strong>N</strong> more lines follow. Each contains two integers <strong>R<sub>i</sub></strong> and <strong>H<sub>i</sub></strong>: the radius and height of the i-th pancake, in millimeters.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>K</strong> ≤ <strong>N</strong>.</li>
	<li>1 ≤ <strong>R<sub>i</sub></strong> ≤ 10<sup>6</sup>, for all i.</li>
	<li>1 ≤ <strong>H<sub>i</sub></strong> ≤ 10<sup>6</sup>, for all i.</li>
	<li>1 ≤ <strong>N</strong> ≤ 10.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the maximum possible total exposed pancake surface area, in millimeters squared. <code>y</code> will be considered correct if it is within an absolute or relative error of 10<sup>-6</sup> of the correct answer.</p>

