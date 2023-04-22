# [Silver IV] Перемешивание - 21417 

[문제 링크](https://www.acmicpc.net/problem/21417) 

### 성능 요약

메모리: 114488 KB, 시간: 112 ms

### 분류

구현, 시뮬레이션, 문자열

### 문제 설명

<p>Петя и Вася играют в забавную игру с карточками. Игра очень простая. Есть колода карт, на каждой из которых написана буква латинского алфавита. Карты перемешиваются, выдаются участникам и они составляют из них слова.</p>

<p>Вася хочет немножко смухлевать. Он знает, в каком порядке лежат карты в колоде и как Петя их мешает. По этим данным он хочет узнать, как будут лежать карты после перемешивания. </p>

<p>Перемешивание карт происходит в несколько этапов. На каждом этапе Петя сначала по очереди берет карты из колоды от верхней к нижней и раскладывает их на две стопки: одну налево, одну направо, одну налево, одну направо. После этого он кладет левую стопку на правую. Эти действия повторяются <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container> раз.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/d6978c54-1ba0-47df-abdc-0c90575d3013/-/preview/" style="width: 563px; height: 142px;"></p>

<p>Помогите Васе определить, как будут лежать карты в колоде после перемешивания.</p>

### 입력 

 <p>Первая строка входного файла содержит строку, описывающую состояние колоды до перемешивания. Строка состоит из заглавных латинских букв. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>-я буква строки соответствует <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>i</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$i$</span></mjx-container>-й карте от низа колоды. Длина строки не превышает 100 символов.</p>

<p>Вторая строка содержит целое число <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$k$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D458 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>k</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1\le k\le 100$</span></mjx-container>).</p>

### 출력 

 <p>В выходной файл выведите состояние колоды после перемешивания в том же формате, что и во входном файле.</p>

