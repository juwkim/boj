# [Silver III] Пароль от сейфа - 29075 

[문제 링크](https://www.acmicpc.net/problem/29075) 

### 성능 요약

메모리: 117504 KB, 시간: 124 ms

### 분류

많은 조건 분기, 문자열

### 제출 일자

2024년 6월 20일 01:28:59

### 문제 설명

<p>Во время первого своего задания Дэдпул понял, что даже с его регенерацией без оружия врагов так просто не одолеть. Поэтому он решил, что настало время открыть сейф, в котором он хранил свое оружие. </p>

<p>Но просто как всегда не получилось. На сейфе оказался замок с кодом, который Дэдпул забыл. Все, что он помнил --- код замка представляет собой палиндром из строчных латинских букв. Дэдпул заметил, что сейчас на замке набрана комбинация, очень похожая на нужную, но что-то все равно не так. Так как у него и своих дел хватает, он хочет потратить на взлом замка как можно меньше времени, а именно рассчитывает получить правильную комбинацию, поменяв местами не более двух символов. </p>

<p>С этой задачей он и обратился к вам. Помогите супергерою --- скажите, можно ли из набранной комбинации получить палиндром таким способом. </p>

### 입력 

 <p>В единственной строке входного файла содержится строка <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-texatom space="4" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi><mjx-texatom texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c7C"></mjx-c></mjx-mo></mjx-texatom><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow><mi>s</mi><mrow data-mjx-texclass="ORD"><mo stretchy="false">|</mo></mrow><mo>≤</mo><msup><mn>10</mn><mn>5</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le |s| \le 10^5$</span></mjx-container>), состоящая из строчных латинских букв.</p>

### 출력 

 <p>В единственной строке выходного файла выведите <<<code>YES</code>>>, если из строки <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container> можно получить палиндром, поменяв не более двух символов местами и <<<code>NO</code>>> в противном случае.</p>

