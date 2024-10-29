# [Bronze III] Building Pyramids - 32585 

[문제 링크](https://www.acmicpc.net/problem/32585) 

### 성능 요약

메모리: 108080 KB, 시간: 96 ms

### 분류

수학

### 제출 일자

2024년 10월 29일 16:26:56

### 문제 설명

<p>At long last, the cats have finally set aside their squabbles with the coatis and the bees. They decide to build a monument to commemorate the end of their feud. To show that such different animals can live together in harmony, the Great Architect Principal Coati decides that this monument should consist of two completely different three-dimensional shapes: the triangular pyramid (for having very sharp corners) and the sphere (for having no corners at all). The idea is to create a large regular tetrahedron out of many small spheres, similar to the one shown in Figure B.1.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/1fa91653-a93c-429a-ac21-e0a114ccfcdb/-/preview/" style="width: 300px; height: 225px;"></p>

<p style="text-align: center;">Figure B.1: A triangular pyramid of spheres, corresponding to the second sample input. One edge of the pyramid contains <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5$</span></mjx-container> spheres, so the entire pyramid consists of <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>35</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$35$</span></mjx-container> spheres.</p>

<p style="text-align: center;"><small>Image CC BY-NC 2.0 by Amafirlian on <a href="https://www.flickr.com/photos/amafirlian/355893316">Flickr</a></small></p>

<p>Alicia the coati, Beesworth the bee, and Darabella the cat would like this monument to be as large as possible. They have designated a piece of land to place the monument on, and have determined how many spheres should be in one of the edges based on where the monument will be placed. How many spheres will the entire pyramid contain, knowing the number of spheres in one of the edges?</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c36"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><msup><mn>10</mn><mn>6</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1\leq n\leq 10^6$</span></mjx-container>), the number of spheres in one of the edges of the pyramid.</li>
</ul>

### 출력 

 <p>Output the number of spheres in the entire pyramid.</p>

