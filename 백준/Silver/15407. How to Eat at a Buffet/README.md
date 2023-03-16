# [Silver IV] How to Eat at a Buffet - 15407 

[문제 링크](https://www.acmicpc.net/problem/15407) 

### 성능 요약

메모리: 115108 KB, 시간: 136 ms

### 분류

그리디 알고리즘

### 문제 설명

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15407/1.png" style="height:194px; width:267px"></p>

<p>Instead of a seated meal, some restaurants offer all-you-can-eat buffet lunches and dinners. This is usually a bargain for famished students. Alice likes such buffet meals, but is always worried about how best to fill her plate with food. She values the n different items on the menu differently, and her goal is to have as much value as she can on her plate, constrained by the limited area of the plate and the limited availability of some menu items. Luckily, items on the menu are easily dividable and Alice can take an arbitrary fraction of each dish. Can you help her fill her plate?</p>

### 입력 

 <p>The input is formed of n + 2 lines:</p>

<ul>
	<li>the first line consists of the number n of different items on the menu;</li>
	<li>the second line consists of the area a of Alice’s plate, an integer in mm<sup>2</sup>;</li>
	<li>each of the n remaining lines consists of information about a menu item, as two integers separated with a space; the first one is the value v<sub>i</sub> of item i per mm<sup>2</sup>, as perceived by Alice; the second one is the area a<sub>i</sub>, in mm<sup>2</sup>, that item i would occupy if Alice were to transfer it fully to her plate.</li>
</ul>

<p>Limits</p>

<ul>
	<li>1 ≤ n ≤ 1 000</li>
	<li>0 ≤ a ≤ 100 000</li>
	<li>For every 0 ≤ i ≤ n − 1:
	<ul>
		<li>0 ≤ v<sub>i</sub> ≤ 100;</li>
		<li>0 ≤ a<sub>i</sub> ≤ 100 000 000.</li>
	</ul>
	</li>
</ul>

### 출력 

 <p>A single line consisting of an integer: the maximal value that Alice can fit on her plate.</p>

