# [Silver IV] Посевные работы - 30729 

[문제 링크](https://www.acmicpc.net/problem/30729) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

그리디 알고리즘, 수학

### 제출 일자

2024년 6월 15일 17:26:30

### 문제 설명

<p>На дворе уже ранняя весна, а Бомбослав только что получил диплом заключительного этапа Открытой олимпиады школьников по программированию и сейчас находится на даче, помогая своему дедушке Пафнутию Максимовичу засеять огород.</p>

<p>Огород представляет собой прямоугольник размеров <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D464 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c210E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi><mo>×</mo><mi>h</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$w \times h$</span></mjx-container>, где <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D464 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$w$</span></mjx-container> и <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c210E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$h$</span></mjx-container> --- целые числа. В этом году Пафнутий Максимович решил засеять огород репой и редькой. При этом он хочет для каждого из растений выделить некоторую область огорода в виде квадрата с целой длиной стороны, причём ориентированного таким образом, что стороны квадрата параллельны сторонам огорода. Квадраты могут иметь разные размеры, но они не должны выходить за пределы огорода и не могут пересекаться по ненулевой площади.</p>

<p>Бомбослав хочет продемонстрировать дедушке, что не зря получил диплом Олимпиады, и поэтому он решил вычислить, какую максимальную площадь огорода можно засеять указанным способом. Поскольку репу дедушка Бомбослава любит меньше, чем редьку, разрешается не сеять её вовсе (то есть использовать только одну квадратную область), если это позволит покрыть б\'{о}льшую площадь огорода. </p>

### 입력 

 <p>В единственной строке входных данных записаны два целых числа <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D464 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>w</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$w$</span></mjx-container> и <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c210E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>h</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$h$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D464 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c210E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>w</mi><mo>,</mo><mi>h</mi><mo>≤</mo><msup><mn>10</mn><mn>9</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq w, h \leq 10^9$</span></mjx-container>) --- размеры огорода.</p>

### 출력 

 <p>Выведите одно целое число --- максимальную площадь огорода, которую можно засеять, выделив одну или две квадратных области описанного в условии вида с максимально возможной суммарной площадью.</p>

