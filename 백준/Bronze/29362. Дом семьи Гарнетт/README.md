# [Bronze II] Дом семьи Гарнетт - 29362 

[문제 링크](https://www.acmicpc.net/problem/29362) 

### 성능 요약

메모리: 148812 KB, 시간: 196 ms

### 분류

수학

### 제출 일자

2025년 3월 8일 04:36:14

### 문제 설명

<p>Совсем недавно семья Гарнетт переехала в новый город. Земельный участок, приобретенный ими, находится рядом с домом, в котором живут Шерлок Холмс и доктор Ватсон. Гарнетты рады такому знакомству, ведь теперь в случае загадочных и необъяснимых происшествий у них будет возможность посоветоваться со знаметитым сыщиком.</p>

<p>Однако, в проблеме, стоящей перед Гарнеттами сейчас, нет ничего загадочного. Участок, на котором они планируют строить себе дом, имеет форму прямоугольника размеров <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>×</mo><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n \times m$</span></mjx-container> метров. Гарнетты, как и все истинные англичане, любят порядок, и поэтому они хотят, чтобы их дом также имел прямоугольную форму, его стены были параллельны сторонам участка, а расстояние от любой стены дома до параллельной ей границы участка было бы целым числом метров. При этом они, конечно же, хотят построить дом максимальной площади.</p>

<p>К сожалению, есть проблема, мешающая им построить дом, совпадающий границами с участком. Заключается она в том, что на участке расположены две скважины с водой, и Гарнетты хотят, чтобы одна из них оказалась внутри дома, а другая --- за его пределами. Чтобы узнать максимальную площадь, которую может иметь дом, отвечающий описанным выше требованиям, они обратились к Шерлоку Холмсу. Помогите ему ответить им на этот вопрос.</p>

### 입력 

 <p>Для удобства разобьем участок на <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi><mo>×</mo><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n \times m$</span></mjx-container> квадратов единичной площади. Каждая из скважин находится ровно в одном квадрате и полностью его занимает. Скважины находятся в разных квадратах. Вершины дома совпадают с вершинами квадратов. </p>

<p>В первой строке даны два числа <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> и <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m$</span></mjx-container> --- размеры участка (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>≤</mo><mi>n</mi><mo>,</mo><mi>m</mi><mo>≤</mo><mn>1000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2 \le n, m \le 1000$</span></mjx-container>). Каждая из <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> последующих строк содержит по <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m$</span></mjx-container> чисел --- описания квадратов единичной площади. Если в данном квадрате расположена скважина, то соответствующее число равно единице, иначе число равно нулю. Гарантируется, что на участке ровно две скважины (ровно два числа, описывающих квадраты единичной площади, равны единице).</p>

### 출력 

 <p>Выведите одно число --- максимальную площадь дома, отвечающего всем требованиям семьи Гарнетт.</p>

