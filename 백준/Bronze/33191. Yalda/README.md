# [Bronze IV] Yalda - 33191 

[문제 링크](https://www.acmicpc.net/problem/33191) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

구현

### 제출 일자

2025년 1월 16일 07:02:26

### 문제 설명

<p><strong>Yalda</strong> is an ancient Persian celebration that marks the longest night of the year, corresponding to the winter solstice. The word Yalda originates from the Syriac language and means <strong>birth</strong>, signifying the rebirth of the sun as days gradually grow longer after the solstice.</p>

<p>On Yalda night, Iranian families come together to spend the night sharing stories, reading poetry (especially works of Persian poets like Hafez), and enjoying each other’s company. The celebration is accompanied by traditional items, including:</p>

<ul>
	<li><strong>Watermelon</strong>: Representing the warmth of summer and warding off winter’s chill.</li>
	<li><strong>Pomegranates</strong>: Symbolizing the cycle of life and prosperity.</li>
	<li><strong>Nuts</strong>: A treat that embodies abundance and blessings.</li>
</ul>

<p>Mahya, busy organizing the ICPC regional contest, has missed celebrating Yalda night with her family. However, she doesn’t want to miss out entirely and plans to celebrate with her friends at the university. To make the gathering more festive, Mahya wants to buy <strong>exactly one</strong> traditional item for the celebration. Due to her limited budget, she needs to carefully decide which item to buy.</p>

<p>The items should be selected based on their price and her preferences. Watermelon is the first choice, pomegranates are the second choice, and nuts are the third choice. If Mahya’s budget does not allow her to buy any of the items, she will skip the purchase entirely.</p>

### 입력 

 <p>The input consists of the following:</p>

<ul>
	<li>The first line contains an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$b$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>b</mi><mo>≤</mo><msup><mn>10</mn><mn>6</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \le b \le 10^6$</span></mjx-container>), representing Mahya’s budget in Rials.</li>
	<li>The next three lines contain the prices of watermelon, pomegranates, and nuts, respectively, each as a non-negative integer not exceeding <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>6</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^6$</span></mjx-container>.</li>
</ul>

### 출력 

 <p>Print the name of the first item Mahya can afford from her preference list: “<code>Watermelon</code>”, “<code>Pomegranates</code>”, or “<code>Nuts</code>”. If her budget is not sufficient for any of the items, output “<code>Nothing</code>”.</p>

