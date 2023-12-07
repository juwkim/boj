# [Silver IV] Дерево - 29236 

[문제 링크](https://www.acmicpc.net/problem/29236) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

수학, 트리

### 제출 일자

2023년 12월 8일 00:06:11

### 문제 설명

<p>Остап Бендер нашел новое применение своим безграничным талантам, а имненно, решил удариться в бизнес. На современном рынке полно всяких товаров, однако его это не смущает, ведь он торгует не чем-нибудь, а корневыми деревьями. </p>

<p>Всем известно, что цена корневого дерева --- это сумма глубин его листов. Корень дерева имеет глубину 0, а глубина любой другой вершины равна глубине ее предка плюс один. У Остапа никогда не возникало проблем с тем, чтобы определить цену дерева, глядя на него, но вот строить дорогие деревья он не умеет.</p>

<p>У нашего героя есть <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> вершин, и целых <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>−</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N-1$</span></mjx-container> ребро. Он может построить из них одно, или несколько деревьев, а потом продать. Помогите Остапу, найдите максимальную суммарную стоимость построеных деревьев.  </p>

### 입력 

 <p>Первая строка входного файла содержит единственное число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c38"></mjx-c></mjx-mn><mjx-texatom texclass="ORD"><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle></mjx-texatom><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c38"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn><mjx-texatom texclass="ORD"><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle></mjx-texatom><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c34"></mjx-c></mjx-mn><mjx-texatom texclass="ORD"><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle></mjx-texatom><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c39"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>8</mn><mrow data-mjx-texclass="ORD"><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle></mrow><mn>589</mn><mrow data-mjx-texclass="ORD"><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle></mrow><mn>934</mn><mrow data-mjx-texclass="ORD"><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle></mrow><mn>591</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1\le N\le 8{\,}589{\,}934{\,}591$</span></mjx-container>) --- количество вершин, которые есть у Остапа.</p>

### 출력 

 <p>Выведите одно число --- максимальная суммарная цена построеных деревьев.</p>

