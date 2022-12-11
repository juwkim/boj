# [Silver IV] Rainbow Beads - 17164 

[문제 링크](https://www.acmicpc.net/problem/17164) 

### 성능 요약

메모리: 115464 KB, 시간: 192 ms

### 분류

슬라이딩 윈도우(sliding_window), 문자열(string), 두 포인터(two_pointer)

### 문제 설명

<p>Jaehyun has a bead which consists of <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> jewels arranged from left to right. Each jewel is in one of the three colors: Red, Blue, and Violet, which is represented as a single character <code>R</code>, <code>B</code>, <code>V</code>. As one of the committees in an important contest, Jaehyun wants to use it as a souvenir for some participant.</p>

<p>Jaehyun likes a bead with diverse colors, so he defines a bead beautiful if every adjacent jewel has different colors. For example, <code>RBVBV</code> is a beautiful bead because every adjacent jewel has a different color. <code>V</code> is a beautiful bead because it does not have adjacent pairs. However, <code>RBBV</code> is not a beautiful bead, because two <code>B</code> is adjacent in the string.</p>

<p>Not only Jaehyun likes a bead with diverse colors, but he likes a contest with diversity. This time, Jaehyun wants to make a bead that is also colorful to colorblind people. For convenience, we will only consider three kinds of people in this problem.</p>

<ul type="disc">
	<li>Non-colorblind people, who can tell all three colors.</li>
	<li>Red-colorblind people (<em>Protanopia</em>), who can't tell apart red and violet: They consider violet jewels as red jewels.</li>
	<li>Blue-colorblind people (<em>Tritanopia</em>), who can't tell apart <s>red</s> blue and violet: They consider violet jewels as blue jewels.</li>
</ul>

<p>In this case, the string <code>RVB</code> is colorful for non-colorblind people, but it is not colorful for red-colorblind people as red and violet jewels are adjacent, and it is also not colorful for blue-colorblind people as violet and blue jewels are adjacent.</p>

<p>Jaehyun wants to pick some contiguous part of the bead and cut it out to give as a souvenir. The part Jaehyun cuts should be colorful to all three kinds of people. Note that, if the whole bead is beautiful, then Jaehyun does not necessarily cut it out, but just give the whole bead. What is the length of the longest bead he can give?</p>

### 입력 

 <p>The first line contains an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>, denoting the length of the bead.</p>

<p>The next line contains string of length <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>, where every character is either <code>R</code>, <code>B</code>, or <code>V</code>.</p>

### 출력 

 <p>Print the maximum possible length of contiguous beads, which is colorful for all three kinds of people.</p>

