# [Silver V] Alice in the Digital World - 17057 

[문제 링크](https://www.acmicpc.net/problem/17057) 

### 성능 요약

메모리: 170608 KB, 시간: 348 ms

### 분류

구현

### 문제 설명

<p>After returning from the Wonderland, Alice needs to improve her scientific skills in this current digital world. Alice decides to participate the ACM-ICPC Asia Nha Trang Regional Contest 2016 to evaluate her actual performance. Her most favorite problem in the contest is following.</p>

<p>Given an array of positive integers A = a<sub>1</sub>, a<sub>2</sub>,…, a<sub>n</sub>, a subarray A<sub>i,j</sub> of A is a sequence of<br>
continuous elements in A, i.e., A<sub>i,j</sub> = a<sub>i</sub>, a<sub>i+1</sub>,…, a<sub>j</sub> (where 1 ≤ i ≤ j ≤ n). The weight of Ai,j is the sum of all its elements,</p>

<p>Given an integer m, your task is to find the maximum weight subarray of <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D434 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>A</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">\(A\)</span></mjx-container> that contains only one m as the minimum element. You can assume that A always contains at least one element with value m.</p>

### 입력 

 <p>The input consists of several datasets. The first line of the input contains the number of datasets, which is a positive number and is not greater than 20. The following lines describe the datasets.</p>

<p>Each dataset is described by the following lines:</p>

<ul>
	<li>The first line contains 2 positive integers n and m (n ≤ 10<sup>5</sup>; m ≤ 2<sup>6</sup>).</li>
	<li>The second line contains n positive integers, each with value at most 2<sup>6</sup>.</li>
</ul>

### 출력 

 <p>For each dataset, write out on one line the found maximum weight.</p>

