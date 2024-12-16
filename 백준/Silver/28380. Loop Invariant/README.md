# [Silver II] Loop Invariant - 28380 

[문제 링크](https://www.acmicpc.net/problem/28380) 

### 성능 요약

메모리: 116404 KB, 시간: 124 ms

### 분류

애드 혹, 문자열

### 제출 일자

2024년 12월 17일 01:50:35

### 문제 설명

<p>Luna, a historian, was exploring the archives of an old monastery when she stumbled on a mysterious scroll of parchment. On it were only two types of symbols: '<code>(</code>' and '<code>)</code>'. Soon she noticed that the sequence of symbols satisfies an interesting property: It can be constructed by repeatedly inserting '<code>()</code>' at some position into an initially empty sequence. Historians call such sequences <em>balanced</em>. Figure L.1 gives an example of a balanced sequence.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/a7000f77-3955-4776-808e-0088db25ed1a/-/preview/" style="width: 450px; height: 20px;"></p>

<p style="text-align: center;">Figure L.1: Sample Input 2 derived by successively inserting '<code>()</code>' into an initially empty sequence.</p>

<p>The chief librarian of the monastery recently told Luna that some of the more elitist monks in the region had a habit of writing on circular pieces of parchment. In their minds, anyone incapable of immediately telling where the text on such a scroll started was also unworthy of knowing its content. Consequently, Luna quickly inspected the edges of her parchment strip. And sure enough, the edges at the left and right end of the parchment strip fit together perfectly, indicating that the parchment once actually was circular. While holding the left and right edges together and looking at the now circular parchment, she wonders whether the balanced sequence starting at the tear is the only such sequence that could have resulted from tearing the parchment apart. After all, it makes little sense trying to decrypt a text when you do not even know where it starts.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with a balanced sequence <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-texatom space="4" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi><mjx-texatom texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>≤</mo><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow><mi>s</mi><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow><mo>≤</mo><msup><mn>10</mn><mn>6</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2\leq |s|\leq 10^6$</span></mjx-container>), the sequence on Luna's strip of parchment.</li>
</ul>

### 출력 

 <p>Output "<code>no</code>" if there is no way to obtain a different balanced sequence by cutting the circular sequence, otherwise give any such sequence.</p>

