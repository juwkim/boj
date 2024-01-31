# [Bronze II] #TheDress - 31368 

[문제 링크](https://www.acmicpc.net/problem/31368) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

사칙연산, 구현, 수학, 문자열

### 제출 일자

2024년 1월 31일 22:38:07

### 문제 설명

<p>After landing on planet i1c5l people noticed that blue and black clothes are quite popular among the locals. Each aboriginal has at least one blue-and-black piece of clothing in their wardrobe. This makes no interest except one curious detail: the locals claimed that these colors weren’t blue and black but white and gold.</p>

<p>Thus a simple test was created to differ a human being from an alien. On one of the wedding parties people took a picture of the blue-and-black groom mother’s dress. This picture was shown to some respondents who were asked the color of the dress. If the answer contained <<blue>> and <<black>> then there was no doubt that the respondent was from the Earth. The answer containing <<white>> and <<gold>> pointed to the person of planet i1c5l origin. If the answer contained neither of word pairs then it was clear that the respondent was a creature from another planet.</p>

<p>You have the complete survey log from planet i1c5l. Your task is to determine the constitution of the planet’s population based on the survey.</p>

### 입력 

 <p>The first line contains single integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> --- the number of respondents (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le N \le 100$</span></mjx-container>). The following <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> lines contain the answers. No line is empty and no line is longer than 100 characters. The answer contains only lower-case Latin letters and spaces. It is guaranteed that no answer can contain <<blue>>, <<black>>, <<white>>, and <<gold>> simultaneously.</p>

### 출력 

 <p>Output three numbers that describe the planet’s population, each on separate line.</p>

<p>The first number --- percentage of earthlings in population.</p>

<p>The second number --- percentage of aboriginals in population.</p>

<p>The third number --- percentage of another planet creatures in population.</p>

<p>Output all numbers with <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-texatom size="s" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-texatom></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mrow data-mjx-texclass="ORD"><mo>−</mo><mn>5</mn></mrow></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^{-5}$</span></mjx-container> accuracy.</p>

