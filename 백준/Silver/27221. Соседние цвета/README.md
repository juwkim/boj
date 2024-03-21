# [Silver IV] Соседние цвета - 27221 

[문제 링크](https://www.acmicpc.net/problem/27221) 

### 성능 요약

메모리: 113840 KB, 시간: 176 ms

### 분류

브루트포스 알고리즘, 자료 구조, 해시를 사용한 집합과 맵, 문자열, 트리를 사용한 집합과 맵

### 제출 일자

2024년 3월 21일 23:42:55

### 문제 설명

<p>Этнограф изучает народ крайнего севера. Его заинтересовала структура бусов, которые составляются из бусин трех цветов: синего, зеленого и красного. Этнографу кажется, что частота, с которой определенные цвета встречаются у соседних бусин, позволяет сделать выводы о культуре народа.</p>

<p>Бусы можно задать в виде строки из заглавных английских букв: <<<code>R</code>>> для красной бусины, <<<code>G</code>>> для зеленой бусины и <<<code>B</code>>> для синей бусины. Соседние буквы в строке соответствуют соседним бусинам. Бусы находятся на круглой нитке, поэтому первая и последняя бусины также являются соседними.</p>

<p>Например, в ожерелье <<<code>RGRGRGRG</code>>> 8 раз рядом встречаются зеленая и красная бусины, а в ожерелье <<<code>RRRR</code>>> 4 раза рядом встречаются две красные бусины.</p>

<p>Помогите этнографу по образцам бусов выяснить, какая пара цветов встречается рядом чаще всего. Порядок цветов в паре не имеет значения.</p>

### 입력 

 <p>На первой строке ввода находится чиcло <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> --- количество бус в распоряжении этнографа (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n \le 100$</span></mjx-container>).</p>

<p>На каждой из следующих строк находится строка из букв <<<code>R</code>>>, <<<code>G</code>>> и <<<code>B</code>>>. Длина каждой строки не меньше <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container> и не больше <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1000$</span></mjx-container>.</p>

### 출력 

 <p>Выведите одну или более строк по два символа: бусины каких двух цветов наибольшее число раз встречаются рядом. Если несколько пар бусин встречаются рядом одинаково часто, необходимо вывести все такие пары, по одной на строке, в любом порядке. Цвета в паре можно выводить в любом порядке.</p>

